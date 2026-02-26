# Stage 1: Basic Calculator

num1 = float(input('Enter The First Number:'))
num2 = float(input('Enter The Second Number:'))
operator = input('Enter The Operator (+, -, *, /): ')

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operator."

print("Result:", result)