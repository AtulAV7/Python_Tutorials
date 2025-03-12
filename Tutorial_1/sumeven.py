def sum_of_even_numbers(n, numbers):
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
    return even_sum

n = int(input("Enter the number of elements: "))
numbers = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

result = sum_of_even_numbers(n, numbers)
print(f"Sum of even numbers: {result}")