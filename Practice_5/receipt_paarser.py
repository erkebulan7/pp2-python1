import re
import json
from datetime import datetime


def read_receipt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def extract_prices(text):
    """
    Extract prices like:
    12.99
    5.50
    100.00
    """
    price_pattern = r"\b\d+\.\d{2}\b"
    prices = re.findall(price_pattern, text)
    return [float(p) for p in prices]


def extract_products(text):
    """
    Extract product names assuming format:
    PRODUCT_NAME   12.99
    """
    product_pattern = r"([A-Za-z\s\-\&]+)\s+\d+\.\d{2}"
    matches = re.findall(product_pattern, text)

    products = []
    for m in matches:
        name = m.strip()
        if name and name.lower() not in ["total", "subtotal", "tax"]:
            products.append(name)

    return products


def extract_datetime(text):
    """
    Match common date/time formats
    """
    date_pattern = r"\b\d{1,2}[\/\-]\d{1,2}[\/\-]\d{2,4}\b"
    time_pattern = r"\b\d{1,2}:\d{2}(?:\s?[APMapm]{2})?\b"

    date = re.search(date_pattern, text)
    time = re.search(time_pattern, text)

    return {
        "date": date.group(0) if date else None,
        "time": time.group(0) if time else None
    }


def extract_payment_method(text):
    methods = [
        "cash",
        "credit",
        "debit",
        "visa",
        "mastercard",
        "amex",
        "card",
        "apple pay",
        "google pay"
    ]

    lower_text = text.lower()

    for method in methods:
        if method in lower_text:
            return method.upper()

    return "UNKNOWN"


def calculate_total(prices):
    return round(sum(prices), 2)


def parse_receipt(file_path):
    text = read_receipt(file_path)

    prices = extract_prices(text)
    products = extract_products(text)
    datetime_info = extract_datetime(text)
    payment_method = extract_payment_method(text)
    total = calculate_total(prices)

    result = {
        "products": products,
        "prices": prices,
        "total_calculated": total,
        "datetime": datetime_info,
        "payment_method": payment_method
    }

    return result


def main():
    receipt_file = "raw.txt"

    parsed_data = parse_receipt(receipt_file)

    print("Parsed Receipt Data:\n")
    print(json.dumps(parsed_data, indent=4))


if __name__ == "__main__":
    main()
