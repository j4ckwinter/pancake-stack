from producer import create_invoice


def invoice_for_order(value):
    return create_invoice(total=value)
