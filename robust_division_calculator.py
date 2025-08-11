 robust_division_calculator.py
 # robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Performs division with robust error handling for ZeroDivisionError and ValueError.

    Args:
        numerator: The number to be divided.
        denominator: The number to divide by.

    Returns:
        The result of the division as a float, or a string with an error message.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Check for division by zero
        if den == 0:
            return "Error: Cannot divide by zero."

        # Perform the division
        result = num / den
        return result
    except ValueError:
        return "Error: Both inputs must be numeric."


