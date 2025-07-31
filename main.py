# calculator.py

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
else:
    print("Error: Invalid operation.")

if 'result' in locals(): # Check if result variable was set
    print(f"{num1} {operation} {num2} = {result}")# calculator.py

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
else:
    print("Error: Invalid operation.")

if 'result' in locals(): # Check if result variable was set
    print(f"{num1} {operation} {num2} = {result}")