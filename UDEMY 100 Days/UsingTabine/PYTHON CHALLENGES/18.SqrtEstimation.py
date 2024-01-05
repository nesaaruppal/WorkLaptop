import math


def bakhshali_square_root(x, max_iter=10):
    """
    Estimates the square root of a number using the Bakhshali method.
    """
    if x < 0:
        raise ValueError("Invalid input")
    z = x
    for i in range(max_iter):
        z = (z + x / z) / 2
        error = z * z - x
        if error < 0.00001:
            return z
    return z


def fixed_point_square_root(x, max_iter=10):
    """
    Estimates the square root of a number using a fixed number of iterations.
    """
    for i in range(max_iter):
        z = (x / (2 * i + 1)) + (x / (2 * i + 2))
        if abs(z - (2 * i + 1) / 2) < 0.00001:
            return z
    return z


if __name__ == "__main__":
    # Prompt the user to enter the number to be squared
    x = float(input("Enter the number: "))

    # Estimate the square root using the Bakhshali method
    bakhshali_root = bakhshali_square_root(x)
    print(
        f"The Bakhshali square root of {x} is approximately {bakhshali_root:.4f}.")

    # Estimate the square root using a fixed number of iterations
    fixed_point_root = fixed_point_square_root(x)
    print(
        f"The fixed-point square root of {x} is approximately {fixed_point_root:.4f}.")

    # Compare the results
    print(
        f"The difference between the Bakhshali and fixed-point methods is {abs(bakhshali_root - fixed_point_root):.4f}.")
