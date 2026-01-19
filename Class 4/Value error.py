try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError as ex:
    print("Exception: ", ex)

print("Please enter a valid integer.")