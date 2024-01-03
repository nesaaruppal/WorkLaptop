# def fact_of_fact(n):
#     """
#     Calculates the factorial of factorials for an integer n.

#     Args:
#         n (int): The integer for which to calculate the factorial of factorials.

#     Returns:
#         int: The factorial of factorials for the given integer n.
#     """
#     # Check if n is less than or equal to 0
#     if n <= 0:
#         return 1

#     # Calculate the factorial of n
#     n_factorial = n * fact_of_fact(n - 1)

#     return n_factorial


# # Test the function with some examples
# print(fact_of_fact(4))  # Output: 288
# print(fact_of_fact(5))  # Output: 34560
# print(fact_of_fact(6))  # Output: 24883200


def factorial(n):

    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


# Driver Code
num = 6
print("Factorial of", num, "is",
      factorial(num))
