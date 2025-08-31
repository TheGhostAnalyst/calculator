# 🧮 Basic Calculator (Python CLI)

A simple **Command-Line Calculator** built in Python that performs basic arithmetic operations using the `pyinputplus` module for input validation. And also saves result to a database for easy recovery of calculation history.

---

## ✨ Features

- ✅ Addition  
- ✅ Subtraction  
- ✅ Multiplication  
- ✅ Division (with zero-division handling)  
- ✅ Exponentiation
- ✅ Logarithm 
- ✅ Continuous operation loop until user exits
- ✅ Saves result to a database for easy recovery of calculation history

---

## 🛠️ Technologies Used

- **Python 3.x**
- **PyInputPlus** – For validated and user-friendly input

---

## 🚀 How to Run

### 1. Clone the Repository


git clone https://github.com/TheGhostAnalyst/calculator.git
cd calculator
### 2. Install Requirements
You must install pyinputplus if it's not already installed:
pip install pyinputplus
### 3. Run the Calculator
python3 calculator.py

📄 Example Usage
Welcome to the Basic Calculator!
This calculator can perform basic arithmetic operations.
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exponential
6. Logarithm
7. View History
8. Exit
Enter choice (1-8): 1
Enter first number: 5
Enter second number: 3
Result: 8
❗ Error Handling
Handles invalid numeric input using pyinputplus.

Checks for division by zero in divide operation.


🧑‍💻 Author
Name: The Ghost Analyst


📄 License
This project is licensed under the MIT License – see the LICENSE file for details.
