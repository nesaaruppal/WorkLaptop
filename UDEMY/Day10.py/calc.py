def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1/n2


num1 = float(input("What is the first number you would like to calculate?: "))
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
for symbols in operations:
    print(symbols)

choice = input("From the symbols: ")

num2 = float(input("What is the second number you would like to calculate: "))
