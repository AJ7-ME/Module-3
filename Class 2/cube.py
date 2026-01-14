num = int(input("What number do you want to cube?\n"))
def cube(num):
    return num * num * num
def by3(num):
    if num % 3 == 0:
        return cube(num)
    else: 
        return False
print(by3(num))
print(by3(4))