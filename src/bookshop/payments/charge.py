def charge(amount, currency="EUR"):
    if amount <= 0:
        raise ValueError("a charge must be positive")
    return {"amount": round(amount, 2), "currency": currency}
