def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return None  # Handle division by zero
    return x / y

def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter an operator (+, -, *, /): ")

        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
            if result is None:
                print("Error: Division by zero is not allowed.")
                return
        else:
            print("Error: Invalid operator.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Error: Please enter valid numbers.")

# Run the calculator
calculator()
