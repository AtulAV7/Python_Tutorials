def calculate_expression(n):
    result = (2 ** (2 * n)) + n + 5
    return result

n = int(input("Enter the value of n: "))
result = calculate_expression(n)
print(f"The value of 2^(2*{n})+{n}+5 = {result}")