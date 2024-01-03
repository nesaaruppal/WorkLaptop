def count_digits(number):
    """
    Counts the number of digits in a number.

    Args:
        number (int or float): The number to count the digits of.

    Returns:
        int: The number of digits in the number.
    """
    # Convert the number to a string
    number_str = str(number)

    # Count the number of characters in the string
    digit_count = len(number_str)

    return digit_count


# Test the function with some numbers
print(count_digits(0))
print(count_digits(4666))  # Output: 4
print(count_digits(544))  # Output: 5
print(count_digits(121317))  # Output: 5
print(count_digits(12345))
print(count_digits(1289396387328))  # Output: 10
