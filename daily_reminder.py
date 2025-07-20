# daily_reminder.py

def daily_reminder():
    """
    Prompts the user for a single task, its priority, and time sensitivity,
    then provides a customized reminder using conditional statements,
    match case, and loops.
    """

    # Prompt for a Single Task
    task = input("Enter your task: ")

    while True:
        priority = input("Priority (high/medium/low): ").lower()
        if priority in ['high', 'medium', 'low']:
            break
        else:
            print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

    while True:
        time_bound = input("Is it time-bound? (yes/no): ").lower()
        if time_bound in ['yes', 'no']:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    # Process the Task Based on Priority and Time Sensitivity
    reminder_message = ""
    immediate_action = ""

    match priority:
        case 'high':
            reminder_message = f"'{task}' is a high priority task"
        case 'medium':
            reminder_message = f"'{task}' is a medium priority task"
        case 'low':
            reminder_message = f"'{task}' is a low priority task"
            if time_bound == 'no':
                immediate_action = ". Consider completing it when you have free time."
            else:
                immediate_action = " that requires attention today!"
        case _: # This case technically won't be hit due to the while loop validation
            reminder_message = f"'{task}' has an unknown priority"

    if time_bound == 'yes' and priority != 'low':
        immediate_action = " that requires immediate attention today!"
    elif time_bound == 'no' and priority != 'low':
        immediate_action = ". You can tackle this at your convenience."


    # Provide a Customized Reminder
    print(f"\nReminder: {reminder_message}{immediate_action}")

if __name__ == "__main__":
    daily_reminder()
