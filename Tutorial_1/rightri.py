a = int(input("Enter the first side length: "))
b = int(input("Enter the second side length: "))
c = int(input("Enter the third side length: "))

if a < b:
    a, b = b, a
if a < c:
    a, c = c, a

if a**2 == b**2 + c**2:
    print("It's a right triangle")
else:
    print("Not a right triangle")
