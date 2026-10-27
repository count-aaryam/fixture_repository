def calculate_total(items, tax_rate):
    subtotal = sum(item["price"] * item["qty"] for item in items)
    return subtotal * (1 + tax_rate)

def apply_discount(total, code):
    if code == "SAVE10":
        return total * 0.9
    return total

def checkout(items, code):
    total = calculate_total(items, 0.18)
    return apply_discount(total, code)

def print_receipt(items):
    return f"Total: {calculate_total(items, 0.18)}"