import pyinputplus as Pyip
import sys
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def exponent(x, y):
    return x ** y

def logarithm(x, base=10):
    if x <= 0:
        return "Error! Logarithm of non-positive number."
    if base <= 0 or base == 1:
        return "Error! Invalid base for logarithm."
    return math.log(x, base)

def calculator():
    while True:
        print("Welcome to the Basic Calculator!")
        print("This calculator can perform basic arithmetic operations.")
        print("""Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exponential
6. Logarithm
7. Exit""")
        
        choice = Pyip.inputInt("Enter choice (1-7): ", min=1, max=7)

        if choice == 7:
            print("Exiting the calculator. Goodbye!")
            sys.exit()

        # For operations 1–5 that need two numbers
        if choice in [1, 2, 3, 4, 5]:
            num1 = Pyip.inputNum("Enter first number: ")
            num2 = Pyip.inputNum("Enter second number: ")
            
            if choice == 1:
                result = add(num1, num2)
            elif choice == 2:
                result = subtract(num1, num2)
            elif choice == 3:
                result = multiply(num1, num2)
            elif choice == 4:
                result = divide(num1, num2)
            elif choice == 5:
                result = exponent(num1, num2)

            print(f"Result: {result}\n")

        # Logarithm operation
        elif choice == 6:
            x = Pyip.inputNum("Enter a positive number to take log of: ", greaterThan=0)
            base_input = input("Enter base for logarithm (press Enter for default base 10): ")
            if base_input.strip() == '':
                base = 10
            else:
                try:
                    base = float(base_input)
                    if base <= 0 or base == 1:
                        print("Error! Base must be > 0 and ≠ 1.\n")
                        continue
                except ValueError:
                    print("Invalid base input.\n")
                    continue

            result = logarithm(x, base)
            print(f"Result: {result}\n")

# Run the calculator
calculator()
