def sum_of_cubes_of_even(n):
    total = 0
    for i in range(2, n+1, 2): 
        total += i**3
    return total

n = int(input("Enter a positive integer: "))
result = sum_of_cubes_of_even(n)
print(f"Sum of cubes of even numbers up to {n}: {result}")