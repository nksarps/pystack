from .errors import InvalidDataError

def validate_amount(amount):
    if not amount:
        raise InvalidDataError("Amount is required")
    
    if isinstance(amount, int) or isinstance(amount, float):
        if amount < 0:
            raise InvalidDataError("Amount cannot be negative")
        return amount
    else:
        raise InvalidDataError("Amount should be a number")