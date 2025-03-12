n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

if len(numbers) % 2 == 0:
    median = (numbers[len(numbers)//2 - 1] + numbers[len(numbers)//2]) / 2
else:
    median = numbers[len(numbers)//2]

print(f"Median: {median}")