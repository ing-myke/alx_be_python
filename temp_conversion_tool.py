# temp_conversion_tool.py

# Define Global Conversion Factors
# Factor for converting Fahrenheit to Celsius: (F - 32) * 5/9
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

# Factor for converting Celsius to Fahrenheit: (C * 9/5) + 32
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit: float) -> float:
    """
    Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    # Use the global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius: float) -> float:
    """
    Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    # Use the global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """
    Handles user interaction for temperature conversion.
    Prompts for temperature and unit, then displays the converted value.
    """
    print("--- Temperature Conversion Tool ---")

    while True:
        try:
            temp_input = input("Enter the temperature value: ")
            temperature = float(temp_input)
            break # Exit loop if temperature is a valid float
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

    while True:
        unit = input("Is this temperature in Celsius (C) or Fahrenheit (F)? ").strip().upper()
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted_temp:.2f}°F")
            break
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted_temp:.2f}°C")
            break
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
