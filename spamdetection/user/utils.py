import re
def validate_phone_number(phone):
    pattern = r"^\+[1-9]\d{1,14}$"
    return bool(re.match(pattern, phone))
