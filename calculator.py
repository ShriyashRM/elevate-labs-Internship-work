# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def calculator():
    print("Welcome to the CLI Calculator 🧮")
    print("Operations: +, -, *, /")
    print("Type 'exit' anytime to quit.")
    
    while True:
        operation = input("\nEnter operation (+, -, *, /) or 'exit': ").strip()
        
        if operation.lower() == "exit":
            print("Goodbye! Exiting calculator.")
            break
        
        if operation not in ["+", "-", "*", "/"]:
            print("Invalid operation. Try again.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number input, please enter digits only.")
            continue
        
        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)
        
        print(f"Result: {result}")

if __name__ == "__main__":
    calculator()