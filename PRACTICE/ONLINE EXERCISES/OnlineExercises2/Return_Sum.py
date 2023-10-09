print("Return the sum of two numbers!")

number = (input("Enter a 2 digit number:\n"))

number1 = number[0]
number2 = number[1]

first_digit = int(number1)
second_digit = int(number2)

addition = first_digit + second_digit

print(f"The number you entered was '{number}', so {first_digit} '+' {second_digit} '=' '{addition}'!")