def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter positive integer {i+1}: "))
    numbers.append(num)

prime_numbers = []
composite_numbers = []

for num in numbers:
    if is_prime(num):
        prime_numbers.append(num)
    else:
        composite_numbers.append(num)

print("Prime numbers:", prime_numbers)
print("Composite numbers:", composite_numbers)