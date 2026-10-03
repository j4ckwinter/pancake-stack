import json
import sys


def summarize(values):
    return {"count": len(values), "average": sum(values) / len(values)}


def main():
    print(json.dumps(summarize(json.load(sys.stdin))))


if __name__ == "__main__":
    main()
