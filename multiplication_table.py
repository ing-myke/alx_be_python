# Prompt the user to enter a number
# The input() function reads a string, so we convert it to an integer using int()
number = int(input("Enter a number to see its multiplication table: "))

# Use a for loop to iterate from 1 to 10
# The range(1, 11) function generates numbers from 1 up to (but not including) 11,
# which means it will generate 1, 2, 3, ..., 10.
for i in range(1, 11):
    # Calculate the product of the user's number and the current iteration number (i)
    product = number * i
    
    # Print each line of the multiplication table in the format "X * Y = Z"
    # We use an f-string for easy formatting.
    print(f"{number} * {i} = {product}")
