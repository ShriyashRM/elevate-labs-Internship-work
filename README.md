Markdown: 
Calculator CLI App 🧮

## Overview
This project is a simple **command-line calculator** built with Python.  
It supports basic arithmetic operations: **addition (+), subtraction (-), multiplication (*) and division (/)**.  
The program keeps running until the user decides to exit.

## Features
- User can choose from `+`, `-`, `*`, `/`
- Input two numbers for calculation
- Handles **invalid input** (e.g., typing letters instead of numbers)
- Handles **division by zero** gracefully
- Runs in a loop until user types `exit`

## How to Run
1. Make sure you have [Python](https://www.python.org/) installed (`python --version` to check).
2. Clone or download this repository.
3. Open terminal in the project folder.
4. Run the script:
   ```bash
   python calculator.py

EXAMPLE :
Welcome to the CLI Calculator 🧮
Operations: +, -, *, /
Type 'exit' anytime to quit.

Enter operation (+, -, *, /) or 'exit': +
Enter first number: 10
Enter second number: 5
Result: 15.0

Challenges & Solutions :
Error: Invalid User Input → Solved using try-except to catch non-numeric entries.
Error: Division by Zero → Added condition to return "Error: Division by zero is not allowed."
User accidentally entered wrong operation → Handled by checking for valid symbols before proceeding.

Outcome
A simple, reliable, and user-friendly calculator that works entirely inside the terminal.
Perfect for practicing Python basics, error handling, and command-line interactivity.


