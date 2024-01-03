def get_multiples(num, length):
    """
    Returns a list of multiples of a given number until the list length reaches a specified length.

    Args:
        num (int): The number to use as the multiplier.
        length (int): The desired length of the returned list.

    Returns:
        list: A list of multiples of `num` until the list length reaches `length`.

    """
    if length <= 0:
        raise ValueError("Length must be a positive integer")

    multiples = []
    current_multiple = num
    while len(multiples) < length:
        multiples.append(current_multiple)
        current_multiple += num

    return multiples

print(get_multiples(7, 5))
print(get_multiples(12, 10))
print(get_multiples(17, 8))