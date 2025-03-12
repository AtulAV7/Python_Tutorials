x = int(input("Enter the x-coordinate: "))
y = int(input("Enter the y-coordinate: "))

if x > 0 and y > 0:
    print("The point is in Quadrant 1")
elif x < 0 and y > 0:
    print("The point is in Quadrant 2")
elif x < 0 and y < 0:
    print("The point is in Quadrant 3")
elif x > 0 and y < 0:
    print("The point is in Quadrant 4")
elif x == 0 and y == 0:
    print("The point is at the Origin")
elif x == 0:
    print("The point lies on the Y-axis")
elif y == 0:
    print("The point lies on the X-axis")
