import math
'''
We created a calculator assignment in the previous assignment. You need to update that calculator using functions. 
Write a Python script for a calculator using functions.Create separate functions for addition, subtraction, 
multiplication, and division functions taking input as parameters and returning the result of the operation performed.
Validate division by zero.Use input from the user to select an operation and numbers.

'''

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
# Additionally, you can also create any more functions you like to improve the calculator functionality.
# Additional Functions
def modulus(x, y):
    return x % y

def exponentiate(x, y):
    return x ** y

def square(x):
    return x ** 2

def square_root(x):
    if x < 0:
        return "Error: Negative number"
    return math.sqrt(x)

def cube(x):
    return x ** 3

def cube_root(x):
    return x ** (1/3)

def absolute_value(x):
    return abs(x)

def factorial(x):
    if x < 0:
        return "Error: Negative number"
    return math.factorial(x)

def power_of_ten(x):
    return 10 ** x

def calculator():
    while True:
        print("================================================================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power of 10")
        print("6. Modulus")
        print("7. Exponentiation")
        print("8. Square")
        print("9. Square Root")
        print("10. Cube")
        print("11. Cube Root")
        print("12. Absolute Value")
        print("13. Factorial")
        
        print("================================================================")

        print("99. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 99:
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            result = add(num1, num2)
            print(f"Result: {result}")
        elif choice == 2:
            result = subtract(num1, num2)
            print(f"Result: {result}")
        elif choice == 3:
            result = multiply(num1, num2)
            print(f"Result: {result}")
        elif choice == 4:
            result = divide(num1, num2)
            print(f"Result: {result}")
        elif choice == 5:
            result = power_of_ten(num1)
            print(f"Result: {result}")
        elif choice == 6:
            result = modulus(num1, num2)
            print(f"Result: {result}")
        elif choice == 7:
            result = exponentiate(num1, num2)
            print(f"Result: {result}")
        elif choice == 8:
            result = square(num1)
            print(f"Result: {result}")
        elif choice == 9:
            result = square_root(num1)
            print(f"Result: {result}")
        elif choice == 10:
            result = cube(num1)
            print(f"Result: {result}")
        elif choice == 11:
            result = cube_root(num1)
            print(f"Result: {result}")
        elif choice == 12:
            result = absolute_value(num1)
            print(f"Result: {result}")
        elif choice == 13:
            result = factorial(num1)
            print(f"Result: {result}")
        
        else:
            print("Invalid choice ")
if __name__ == "__main__":
    calculator()