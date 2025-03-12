def power(x, y):
    if y == 0:
        return 1
    
    result = 1
    for _ in range(y):
        result *= x
    
    return result

x = float(input("Enter the value of X: "))
y = int(input("Enter the value of Y: "))
result = power(x, y)
print(f"{x}^{y} = {result}")