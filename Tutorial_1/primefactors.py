def prime_factors(n):
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    if n > 2:
        factors.append(n)
        
    return factors

number = int(input("Enter a number to find its prime factors: "))
factors = prime_factors(number)
print(f"Prime factors of {number}: {factors}")