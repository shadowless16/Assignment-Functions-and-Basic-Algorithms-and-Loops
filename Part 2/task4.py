def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def calculator():
    print("Simple Calculator")
    print("Type 'exit' to stop the program.")
    
    while True:
        user_input = input("Enter operation (add, subtract, multiply, divide) or 'exit' to quit: ").lower()
        
        if user_input == 'exit':
            print("Exiting the calculator. Goodbye!")
            break 
        
        if user_input in ['add', 'subtract', 'multiply', 'divide']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue  
            
            if user_input == 'add':
                print(f"The result is: {add(num1, num2)}")
            elif user_input == 'subtract':
                print(f"The result is: {subtract(num1, num2)}")
            elif user_input == 'multiply':
                print(f"The result is: {multiply(num1, num2)}")
            elif user_input == 'divide':
                print(f"The result is: {divide(num1, num2)}")
        else:
            print("Invalid operation. Please choose add, subtract, multiply, divide, or type 'exit'.")

calculator()
