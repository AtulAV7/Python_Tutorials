# Program to find nth Fibonacci number using recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter a position to find the Fibonacci number: "))
result = fibonacci(num)
print(f"The {num}th Fibonacci number is {result}")