def total(lines):
    return round(sum(line["quantity"] * line["unit_price"] for line in lines), 2)
