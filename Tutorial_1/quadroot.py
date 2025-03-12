a = int(input("Please enter first value: "))
b = int(input("Please enter second value: "))
c = int(input("Please enter third value: "))

print(f"The quadratic equation is {a}x^2 + {b}x + {c}")


discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("No real roots exist.")
else:
    sqrt_val = discriminant ** (1/2)  
    root1 = (-b + sqrt_val) / (2 * a)
    root2 = (-b - sqrt_val) / (2 * a)

    print(f"The first root is: {root1}\nThe second root is: {root2}")
