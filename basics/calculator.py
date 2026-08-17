a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

process = input("Choose operation (add, subtract, multiply, divide): ")

if process == "add":
    result = a + b
    print("Result:", result)
elif process == "subtract":
    result = a - b
    print("Result:", result)
elif process == "multiply":
    result = a * b
    print("Result:", result)
elif process == "divide":  
    if b != 0:
        result = a / b
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")


users = {
    1234: {"name": "User 1", "age": 10},
    2343: {"name": "User 2", "age": 23},
    7829: {"name": "User 3", "age": 67},
    2982: {"name": "User 4", "age": 23}
}