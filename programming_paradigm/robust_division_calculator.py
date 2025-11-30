def safe_divide(numerator, denominator):
    try:
        # Try converting inputs to float
        num = float(numerator)
        den = float(denominator)

        # Try dividing
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
