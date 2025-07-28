# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtains and displays the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    # Get the current date and time
    current_date = datetime.now()

    # Format and print the current date and time
    print(f"Current Date and Time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    """
    Prompts the user for a number of days, calculates a future date based on
    the current date, and prints it in 'YYYY-MM-DD' format.
    """
    while True:
        try:
            days_to_add_str = input("Enter a number of days to add to the current date: ")
            days_to_add = int(days_to_add_str)
            break # Exit loop if input is a valid integer
        except ValueError:
            print("Invalid input. Please enter an integer for the number of days.")

    # Get the current date (without time for simpler future date calculation)
    current_date_only = datetime.now().date()

    # Calculate the future date by adding the specified number of days
    future_date = current_date_only + timedelta(days=days_to_add)

    # Print the future date
    print(f"Future Date ({days_to_add} days from now): {future_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    print("--- Exploring Python's Datetime Module ---")

    # Part 1: Display the Current Date and Time
    display_current_datetime()

    print("\n" + "="*40 + "\n") # Separator for clarity

    # Part 2: Calculate a Future Date
    calculate_future_date()

    print("\n--- End of Datetime Exploration ---")
