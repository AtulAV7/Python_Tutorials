def calculate_area(radius):
    pi = 3.14159
    area = pi * radius * radius
    return area

radius = float(input("Enter the radius of the circle: "))
area = calculate_area(radius)
print("Area of the circle:", area)