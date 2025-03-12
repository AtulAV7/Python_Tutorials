def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def compute_ncr(n, r):
    if r > n:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))

n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))

result = compute_ncr(n, r)
print(f"{n}C{r} =", result)