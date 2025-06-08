# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global conversion factor"""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global conversion factor"""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    print("Temperature Conversion Tool")
    print("--------------------------")
    
    try:
        # Get temperature input
        temp_input = input("Enter temperature (e.g., '32 C' or '89.6 F'): ").strip().upper()
        if not temp_input:
            raise ValueError("Empty input")
            
        # Split into value and unit
        parts = temp_input.split()
        if len(parts) != 2:
            raise ValueError("Invalid format")
            
        temp_value = float(parts[0])
        temp_unit = parts[1]
        
        # Perform conversion based on unit
        if temp_unit == 'C':
            converted_temp = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {converted_temp:.2f}°F")
        elif temp_unit == 'F':
            converted_temp = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is {converted_temp:.2f}°C")
        else:
            print("Error: Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
            
    except ValueError as e:
        if "could not convert" in str(e):
            print("Error: Invalid temperature. Please enter a numeric value.")
        else:
            print(f"Error: {e}. Please use format '32 C' or '89.6 F'.")

if __name__ == "__main__":
    main()