"""
Input validation utilities
"""

def validate_positive_float(value, name="Input"):
    """
    Validate that a value is a positive float
    """
    try:
        num = float(value)
        if num <= 0:
            raise ValueError(f"{name} must be positive")
        return num
    except ValueError as e:
        if "must be positive" in str(e):
            raise
        raise ValueError(f"{name} must be a valid number")

def validate_coefficient(value, name="Coefficient"):
    """
    Validate lift/drag coefficient
    """
    try:
        num = float(value)
        if num < 0:
            raise ValueError(f"{name} cannot be negative")
        return num
    except ValueError:
        raise ValueError(f"{name} must be a valid number")
