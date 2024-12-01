# Simple Calculator Program
print('Welcome to Calculator!')

# Function Definitions
def add(num1, num2):
    """Return the sum of two numbers."""
    return num1 + num2

def subtract(num1, num2):
    """Return the difference of two numbers."""
    return num1 - num2

def multiply(num1, num2):
    """Return the product of two numbers."""
    return num1 * num2

def divide(num1, num2):
    """Return the division of two numbers."""
    # Handle division by zero
    if num2 == 0:
        return "Error! Division by zero is not allowed."
    return num1 / num2

def modulus(num1, num2):
    """Return the remainder of division of two numbers."""
    return num1 % num2

# Main Loop
while True:
    # Input numbers and operator
    first_number = float(input('Enter the first number: '))
    operator = input('Enter an operator (+, -, *, /, %): ')
    second_number = float(input('Enter the second number: '))

    # Perform the calculation based on the operator
    if operator == '+':
        result = add(first_number, second_number)
    elif operator == '-':
        result = subtract(first_number, second_number)
    elif operator == '*':
        result = multiply(first_number, second_number)
    elif operator == '/':
        result = divide(first_number, second_number)
    elif operator == '%':
        result = modulus(first_number, second_number)
    else:
        print("Invalid operator! Please use one of +, -, *, /, or %.")
        continue

    # Display the result
    print(f"The result of {first_number} {operator} {second_number} is: {result}")

    # Ask the user if they want to perform another calculation
    continue_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
    if continue_calculation != 'yes':
        print("Thank you for using the calculator. Goodbye!")
        break