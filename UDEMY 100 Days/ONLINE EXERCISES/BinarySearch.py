import random

# Generate a list of random numbers
numbers = [random.randint(0, 100) for i in range(10)]

# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Initialize two indices for the start and end of the list
start = 0
end = len(numbers) - 1

# Loop while the start index is less than the end index
while start <= end:
    # Calculate the middle index
    middle = (start + end) // 2

    # Check if the middle index is the number the user entered
    if numbers[middle] == number:
        # Print a message indicating that the number was found
        print(f"The number {number} was found at index {middle}.")
        break

    # Check if the middle index is greater than the number the user entered
    elif numbers[middle] > number:
        # Set the end index to the middle index
        end = middle - 1

    # Check if the middle index is less than the number the user entered
    else:
        # Set the start index to the middle index
        start = middle + 1

# Print a message indicating that the number was not found if the loop ends
print(f"The number {number} was not found in the list.")
