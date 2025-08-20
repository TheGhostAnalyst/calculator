import pyinputplus as Pyip
import sys

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

def calculator():
    while True:
        print("Welcome to the Basic Calculator!")
        print("This calculator can perform basic arithmetic operations.")
        print("Select operation:")
        print("""1. Add
2. Subtract
3. Multiply
4. Divide
5. Exponential          
6. Exit""")
        
        choice = Pyip.inputInt("Enter choice (1/2/3/4/5/6): ", min=1, max=6)

        if choice == 6:
            print("Exiting the calculator. Goodbye!")
            sys.exit()

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

# Run the calculator
calculator()
