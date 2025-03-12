def multiplication_table(n):
    for i in range(1, n+1):
        print(f"\nMultiplication table of {i}:")
        for j in range(1, 11):
            print(f"{i} × {j} = {i*j}")

n = int(input("Enter the value of n: "))
multiplication_table(n)