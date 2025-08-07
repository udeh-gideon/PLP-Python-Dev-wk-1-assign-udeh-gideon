# My Awesome Calculator Program
print('Welcome to my Calculator created using Python Programming!')

# Asks the user to input two numbers
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))

# Prompts the user to input the arithmetic operation
operation = input('Enter an operation (+, -, *, /): ')

# Performs the artithmetic operation and prints the results

# For Addition
if operation == '+':
    result = num1 + num2
    print(f'{num1} + {num2} = {result}')
# For Subtraction
elif operation == '-':
    result = num1 - num2
    print(f'{num1} - {num2} = {result}')
# For Multiplication
elif operation == '*':
    result = num1 * num2
    print(f'{num1} * {num2} = {result}')
# For Division
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f'{num1} / {num2} = {result}')
    else:
        print('Error: Division by zero is not allowed.')
else:
    print('Invalid operation. Please choose +, or -, or *, or /.')