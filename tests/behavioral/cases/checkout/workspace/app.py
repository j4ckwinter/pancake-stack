import os


def quote(subtotal, zone):
    if zone != "local":
        raise ValueError("unknown zone")
    return 0 if subtotal >= 100 else 5


def carrier():
    if not os.environ.get("CARRIER_TOKEN"):
        raise RuntimeError("carrier token missing")
    raise RuntimeError("carrier client unavailable")
