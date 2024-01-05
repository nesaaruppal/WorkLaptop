def decimal_to_binary(n):
    # Check if the input is within the valid range
    if n < 0 or n > 255:
        return "Invalid input"

    # Initialize a string to hold the binary representation
    binary = ""

    # Loop until the decimal number is 0
    while n > 0:
        # Get the last digit of the decimal number
        last_digit = n % 2

        # Append the last digit to the binary representation
        binary = str(last_digit) + binary

        # Shift the decimal number left by 1
        n = n // 2

    # Return the binary representation
    return binary


print(decimal_to_binary(4))
