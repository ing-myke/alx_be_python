# match_case_calculator.py

def main():
    """
    This function implements a simple calculator using match-case statements.
    It prompts the user for two numbers and an operation, then performs the calculation.
    """
    print("Welcome to the Match Case Calculator!")

    try:
        # Prompt for the first number
        num1 = float(input("Enter the first number: "))

        # Prompt for the second number
        num2 = float(input("Enter the second number: "))

        # Prompt for the operation
        operation = input("Choose the operation (+, -, *, /): ")

        result = None
        message = ""

        # Use a match-case statement to perform the selected operation
        match operation:
            case '+':
                result = num1 + num2
                message = f"The result of addition is: {result}"
            case '-':
                result = num1 - num2
                message = f"The result of subtraction is: {result}"
            case '*':
                result = num1 * num2
                message = f"The result of multiplication is: {result}"
            case '/':
                # Handle division by zero
                if num2 == 0:
                    message = "Error: Division by zero is not allowed."
                else:
                    result = num1 / num2
                    message = f"The result of division is: {result}"
            case _:
                # Handle invalid operation input
                message = "Error: Invalid operation chosen. Please use +, -, *, or /."

        # Display the result or error message
        print(message)

    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
