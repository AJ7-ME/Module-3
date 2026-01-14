def circumference(radius):
    pi = 3.14
    return 2 * pi * radius
r = float(input("Enter the radius of the circle: "))
res = circumference(r)
print("The circumference of the circle is:", res)