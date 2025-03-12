def factorial(n):
    if n == 0:
        return 1
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

x = float(input("Enter the value of x (in radians): "))
n_terms = int(input("Enter the number of terms: "))

result = 0
for i in range(n_terms):
    term = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
    result = result + term

print(f"sin({x}) ≈ {result}")