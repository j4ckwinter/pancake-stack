#!/usr/bin/env python3
"""Read model choices from the local Codex app server."""

import argparse
import json
import math
import queue
import subprocess
import sys
import threading
import time


def discover(codex, timeout):
    messages = queue.Queue()
    deadline = time.monotonic() + timeout
    process = subprocess.Popen(
        [codex, "app-server", "--stdio"], stdin=subprocess.PIPE,
        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True,
    )

    def read_messages():
        try:
            for line in process.stdout:
                messages.put(line)
        finally:
            messages.put(None)

    reader = threading.Thread(target=read_messages, daemon=True)
    reader.start()

    def request(identifier, method, params):
        process.stdin.write(json.dumps({"id": identifier, "method": method, "params": params}) + "\n")
        process.stdin.flush()
        while True:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise ValueError("model discovery timed out")
            try:
                line = messages.get(timeout=remaining)
            except queue.Empty:
                raise ValueError("model discovery timed out") from None
            if line is None:
                raise ValueError("Codex app server closed before discovery completed")
            response = json.loads(line)
            if not isinstance(response, dict):
                raise ValueError("invalid app server response")
            if response.get("id") != identifier:
                continue
            if "error" in response:
                error = response["error"]
                message = error.get("message") if isinstance(error, dict) else None
                detail = f": {message.strip()}" if isinstance(message, str) and message.strip() else ""
                raise ValueError(f"Codex rejected {method}{detail}")
            result = response.get("result")
            if not isinstance(result, dict):
                raise ValueError("invalid app server result")
            return result

    try:
        request(1, "initialize", {"clientInfo": {"name": "pancake-stack-setup", "version": "0.1.2"}})
        process.stdin.write('{"method":"initialized"}\n')
        process.stdin.flush()
        models = []
        cursors = set()
        cursor = None
        identifier = 2
        while True:
            result = request(identifier, "model/list", {"cursor": cursor, "includeHidden": False})
            rows = result.get("data")
            if not isinstance(rows, list):
                raise ValueError("invalid model catalog")
            for row in rows:
                if not isinstance(row, dict):
                    raise ValueError("invalid model entry")
                model = row.get("model")
                efforts = row.get("supportedReasoningEfforts")
                if not isinstance(model, str) or not model.strip() or not isinstance(efforts, list):
                    raise ValueError("invalid model entry")
                values = []
                for effort in efforts:
                    value = effort.get("reasoningEffort") if isinstance(effort, dict) else None
                    if not isinstance(value, str) or not value.strip():
                        raise ValueError("invalid reasoning effort")
                    values.append(value)
                models.append({"model": model, "reasoningEfforts": values})
            cursor = result.get("nextCursor")
            if cursor is None:
                break
            if not isinstance(cursor, str) or not cursor or cursor in cursors:
                raise ValueError("invalid catalog pagination")
            cursors.add(cursor)
            identifier += 1
        if not models:
            raise ValueError("Codex returned no model choices")
        return {"models": models}
    finally:
        process.terminate()
        try:
            process.wait(timeout=2)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait()
        process.stdin.close()
        reader.join(timeout=2)
        process.stdout.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex", default="codex", help="Codex executable name or path")
    parser.add_argument("--timeout", type=float, default=15, help="total discovery timeout in seconds")
    args = parser.parse_args()
    if not math.isfinite(args.timeout) or args.timeout <= 0:
        parser.error("timeout must be a positive finite number")
    try:
        print(json.dumps(discover(args.codex, args.timeout), indent=2))
    except (OSError, ValueError, UnicodeError) as error:
        print(f"catalog: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
