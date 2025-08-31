import pyinputplus as Pyip
import sys
import math
from datetime import datetime
import shelve

def save(result2):
    ok = datetime.now().strftime("%Y-%m-%d %H:%M")
    contents = {'history': result2, 'timestamp': ok}
    with shelve.open('calculator_history.db', writeback=True)as db:
        if 'history'  in db:
            db['history'].append(contents)
        else:
            db['history'] = [contents]


def read():
   with shelve.open('calculator_history.db') as db:
         if 'history' in db:
              for entry in db['history']:
                print(f"{entry['timestamp']}: {entry['history']}")
         else:
              print("No history found.")


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
7. View History
8. Exit""")
        
        choice = Pyip.inputInt("Enter choice (1-8): ", min=1, max=8)

        if choice == 8:
            print("Exiting the calculator. Goodbye!")
            sys.exit()

        # For operations 1–5 that need two numbers
        if choice in [1, 2, 3, 4, 5]:
            num1 = Pyip.inputNum("Enter first number: ")
            num2 = Pyip.inputNum("Enter second number: ")
            
            if choice == 1:
                result = num1 + num2
                result1 = f"{num1} + {num2} = {result}"
                save(result1)
                print(result1)

            elif choice == 2:
                result = num1 - num2
                result2 = f"{num1} - {num2} = {result}"
                save(result2)
                print(result2)

            elif choice == 3:
                result = num1 * num2
                result3 = f"{num1} * {num2} = {result}"
                save(result3)
                print(result3)

            elif choice == 4:
                result = num1 / num2
                result4 = f"{num1} / {num2} = {result}"
                save(result4)
                print(result4)

            elif choice == 5:
                result = num1 ** num2
                result5 = f"{num1} ** {num2} = {result}"
                save(result5)
                print(result5)

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

            result = math.log(x, base)
            result6 = f"log base {base} of {x} = {result}"
            print(result6)
            save(result6)

        elif choice == 7:
            read()
            continue

# Run the calculator
calculator()
