


def show_main_menu():
    """
    Displays the main menu with options for:
    - User Login (Book/Cancel/View tickets)
    - Admin Login (Manage buses)
    - Exit
    """
    print("\nChoose an option:\n")
    print("1. 👤 User Login (Book/Cancel Tickets)")
    print("3. 🚪 Exit")
    print()

def calculator():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        process = input("Choose operation (add, subtract, multiply, divide): ")
        if process == "add":
            result = addition(a, b)
            print("Result:", result)
        elif process == "subtract":
            result = subtract(a, b)
            print("Result:", result)
        elif process == "multiply":
            result = multiply(a, b)
            print("Result:", result)
        elif process == "divide":  
            if b != 0:
                result = divide(a, b)
                print("Result:", result)
            else:
                raise KeyError("Error: Division by zero is not allowed.")
        else:
            print("Choose the Correct Operator")
    except Exception as error:
            print(error)
    return result

def addition(a, b):
    try:
        result = a + b
    except Exception as error:
        print(error)
    return result

def subtract(a, b):
    try:
        result = a - b
    except Exception as error:
        print(error)
    return result

def multiply(a, b):
    try:
        result = a * b
    except Exception as error:
        print(error)
    return result

def divide(a, b):
    try:
        result = a / b
    except Exception as error:
        print(error)
    return result

result = calculator()
print(result)