from config import CURRENCY_ALIASES

def processing(text: str):
    parts = text.split()
    if len(parts) != 2:
        return
    
    amount_raw, currency_input = parts[0].replace(",", "."), parts[1].lower()

    if currency_input not in CURRENCY_ALIASES:
        return
    try:
        amount = float(amount_raw)
    except ValueError:
        return
    return amount, currency_input