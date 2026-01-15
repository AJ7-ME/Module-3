def final_val(x, y):
    return (x - y)
#Asking Info for variables
y = int(input("How much did you HAVE to pay: "))
x = int(input("How much did you pay: "))
final = final_val(x, y)
#How much you owe
if final < 0:
    final = final * -1
    print("You owe the Store/Shop", final)
# If nobody owes anything
elif final == 0:
    print("You owe the Store/Shop $0")
#How much the shopkeeper owes you
elif final > 0:
    print(f"The Store/Shop owes YOU ${final}")