def stats_cart(cart):
    total_amount, total_quantity = 0, 0
    if cart:
        for c in cart.values():
            total_amount += c['quantity'] * c['price']
            total_quantity += c['quantity']

    return {
        "total_quantity": total_quantity,
        "total_amount": total_amount
    }
