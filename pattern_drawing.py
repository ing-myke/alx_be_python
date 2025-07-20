# pattern_drawing.py

# Prompt user for pattern size
while True:
    try:
        size_str = input("Enter the size of the pattern: ")
        size = int(size_str)
        if size > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Draw the pattern
row_count = 0
while row_count < size:
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row_count += 1
