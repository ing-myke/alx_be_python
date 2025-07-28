# shopping_list_manager.py

def shopping_list_manager():
    """
    Manages a simple shopping list, allowing users to add, view, and remove items.
    """
    shopping_list = []  # Initialize an empty list for the shopping list

    while True:
        print("\n--- Shopping List Manager Menu ---")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Add item functionality
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.")
        elif choice == '2':
            # Remove item functionality
            if not shopping_list:
                print("Your shopping list is empty. Nothing to remove.")
                continue

            item_to_remove = input("Enter the item to remove: ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' has been removed from your shopping list.")
            else:
                print(f"'{item_to_remove}' was not found in your shopping list.")
        elif choice == '3':
            # View list functionality
            if not shopping_list:
                print("Your shopping list is currently empty.")
            else:
                print("\n--- Your Shopping List ---")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
        elif choice == '4':
            # Exit functionality
            print("Exiting Shopping List Manager. Goodbye!")
            break
        else:
            # Handle invalid choices
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    shopping_list_manager()
