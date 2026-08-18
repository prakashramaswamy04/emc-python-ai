def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Error: Division by zero is not allowed.")
    return a / b


def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    try:
        num1 = float(input("Enter first number: "))
        op = input("Choose an operation (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))

        if op == "+":
            result = add(num1, num2)
        elif op == "-":
            result = subtract(num1, num2)
        elif op == "*":
            result = multiply(num1, num2)
        elif op == "/":
            result = divide(num1, num2)
        else:
            print("Invalid operator selected.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")
    except ZeroDivisionError as e:
        print(e)


if __name__ == "__main__":
    calculator()
