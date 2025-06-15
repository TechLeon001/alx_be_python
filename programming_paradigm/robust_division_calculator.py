def safe_divide(numerator, denominator):
    """
    Safely divides two numbers with comprehensive error handling.
    
    Args:
        numerator: The numerator (as string or number)
        denominator: The denominator (as string or number)
        
    Returns:
        float: The division result if successful
        str: Error message if division fails
    """
    try:
        # Convert inputs to floats first
        num = float(numerator)
        den = float(denominator)
        
        # Perform the division
        result = num / den
        return result
    except ValueError:
        return "Error: Both inputs must be numbers"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except Exception as e:
        return f"Error: An unexpected error occurred - {str(e)}"