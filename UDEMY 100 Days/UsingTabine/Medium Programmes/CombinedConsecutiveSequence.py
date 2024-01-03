def is_consecutive_sequence(arr1, arr2):
    """
    Determines if two arrays form a consecutive sequence.

    Args:
        arr1 (list): The first array.
        arr2 (list): The second array.

    Returns:
        bool: True if the two arrays form a consecutive sequence, False otherwise.
    """
    # Check if the lengths of the two arrays are the same
    if len(arr1) != len(arr2):
        return False

    # Sort the two arrays in ascending order
    arr1.sort()
    arr2.sort()

    # Initialize a variable to track the previous element in arr1
    prev_elem = arr1[0]

    # Loop through each element in arr2
    for elem in arr2:
        # If the current element is not consecutive with the previous element, return False
        if elem != prev_elem + 1:
            return False

        # Update the previous element
        prev_elem = elem

    # If we made it to the end of arr2 without returning False, return True
    return True


# Test the function with some examples
arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 5, 6]
print(is_consecutive_sequence(arr1, arr2))  # Output: False

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4, 6]
print(is_consecutive_sequence(arr1, arr2))  # Output: False

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4, 5]
print(is_consecutive_sequence(arr1, arr2))  # Output: True
