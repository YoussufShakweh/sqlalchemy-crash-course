import re
from datetime import date, datetime


def validate_name(value):
    if not re.match(r"^[a-zA-Z]+$", value):
        raise ValueError("Invalid, only alphabetic characters allowed")


def validate_email(value):
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", value):
        raise ValueError("Invalid email format")


def validate_birth_date(value):
    if isinstance(value, date):
        value = value
    elif isinstance(value, str):
        value = date.fromisoformat(value)
    else:
        raise ValueError("Invalid date format")

    if value > datetime.now().date():
        raise ValueError("Date can not be in the future")
