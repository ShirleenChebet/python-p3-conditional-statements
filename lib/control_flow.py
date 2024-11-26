#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    return "Access denied"
    pass

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature < 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    return "It's perfect out there!"
    pass

def fizzbuzz(num):
    # your code here
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    return num
    pass

def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        # Ensure we handle division by zero gracefully
        if num2 == 0:
            print("Cannot divide by zero!")
            return None
        return num1 / num2
    else:
        # Print an error message for invalid operations
        print("Invalid operation!")
        return None
    pass
