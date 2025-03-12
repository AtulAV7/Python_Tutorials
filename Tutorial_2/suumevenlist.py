n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

even_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_sum = even_sum + num

print(f"Sum of even numbers: {even_sum}")