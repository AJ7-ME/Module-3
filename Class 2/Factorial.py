num1 = int(input("What do you want to Factorialise?\n"))
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)
num = num1
print (num)
print(factorial.__doc__)
print("The factorial of",num1,"is", factorial(num1))