EXCHANGE_RATES = {
    "USD": 1.0,
    "ILS": 3.68,
    "EUR": 0.92,
}


def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    if amount < 0:
        raise ValueError("סכום לא יכול להיות שלילי")
    
    from_currency = from_currency.strip().upper()
    to_currency = to_currency.strip().upper()

    if from_currency not in EXCHANGE_RATES or to_currency not in EXCHANGE_RATES:
        raise ValueError("מטבע לא נתמך")

    amount_in_usd = amount / EXCHANGE_RATES[from_currency]

    converted_amount = amount_in_usd * EXCHANGE_RATES[to_currency]

    return round(converted_amount, 2)