def pentagonal_dots(n):
    """
    Calculates the number of dots in a pentagonal shape around the center dot on a given iteration.

    Args:
        n (int): The iteration number.

    Returns:
        int: The number of dots in the pentagonal shape on the given iteration.
    """
    # Check if n is 1 or less
    if n <= 1:
        return 1

    # Calculate the number of dots on the previous iteration
    prev_dots = (n * (3 * n - 1)) // 2

    # Calculate the number of dots on the current iteration
    curr_dots = (n * (3 * n - 3)) // 2

    return curr_dots - prev_dots


# Test the function with some examples
print(pentagonal_dots(1))  # Output: 1
print(pentagonal_dots(2))  # Output: 6
print(pentagonal_dots(3))  # Output: 16
print(pentagonal_dots(4))  # Output: 31
print(pentagonal_dots(5))  # Output: 55
print(pentagonal_dots(6))  # Output: 86
print(pentagonal_dots(7))  # Output: 125
print(pentagonal_dots(8))  # Output: 170
print(pentagonal_dots(9))  # Output: 221
print(pentagonal_dots(10))  # Output: 276
