def calculate_delivery_cost(city, weight_kg):
    base_rate = 50.0 if city == "Ivano-Frankivsk" else 110.0
    return base_rate + weight_kg * 12.0


def process_standard_invoice(amount, city, weight_kg, tax_rate=0.20):
    delivery = calculate_delivery_cost(city, weight_kg)
    total = amount * (1 + tax_rate) + delivery
    return {"status": "PROCESSED", "total": round(total, 2)}


def process_tax_exempt_invoice(amount, city, weight_kg):
    delivery = calculate_delivery_cost(city, weight_kg)
    total = amount + delivery
    return {"status": "TAX_EXEMPT", "total": round(total, 2)}
