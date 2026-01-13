def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def expo(x, y):
    return x ** y
def floor(x, y):
    return x // y
print("Please select your opeation")
print("a. Add")
print("B. Subtract")
print("C. Multiply")
print("D. Divide")
print("E. Exponentiation")
print("F. Floor division")
choice1 = input("Please enter your choice (A/B/C/D/E/F): ")
choice = choice1.lower()
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
if choice == "a":
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == "b":
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == "c":
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == "d":
    print(num1, "/", num2, "=", divide(num1, num2))
elif choice == "e":
    print(num1, "**", num2, "=", expo(num1, num2))
elif choice == "f":
    print(num1, "//", num2, "=", floor(num1, num2))
else:
    print("Invalid input")