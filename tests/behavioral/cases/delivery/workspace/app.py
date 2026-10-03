def quote(subtotal, zone):
    if subtotal < 0:
        raise ValueError("subtotal must be nonnegative")
    if zone not in ("local", "remote"):
        raise ValueError("unknown zone")
    if subtotal >= 100:
        return 0
    return 5 if zone == "local" else 12
