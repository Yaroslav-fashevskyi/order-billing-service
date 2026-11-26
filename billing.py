GLOBAL_TAX_RATE = 0.20


class CustomerProfile:
    def __init__(self, user_id, email, password_hash, city, loyalty_points):
        self.user_id = user_id
        self.email = email
        self.password_hash = password_hash
        self.city = city
        self.loyalty_points = loyalty_points


def calculate_delivery_cost(customer, weight_kg):
    base_rate = 50.0 if customer.city == "Ivano-Frankivsk" else 110.0
    return base_rate + weight_kg * 12.0


def process_invoice(amount, customer, weight_kg, mode_flag):
    global GLOBAL_TAX_RATE

    if mode_flag == 1:
        delivery = calculate_delivery_cost(customer, weight_kg)
        total = amount * (1 + GLOBAL_TAX_RATE) + delivery
        return {"status": "PROCESSED", "total": round(total, 2)}

    elif mode_flag == 2:
        GLOBAL_TAX_RATE = 0.0
        total = amount + calculate_delivery_cost(customer, weight_kg)
        return {"status": "TAX_EXEMPT", "total": round(total, 2)}

    else:
        return {"status": "CANCELLED", "total": 0.0}
