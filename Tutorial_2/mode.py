n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

counts = {}
for num in numbers:
    if num in counts:
        counts[num] = counts[num] + 1
    else:
        counts[num] = 1

max_count = 0
mode = None

for num, count in counts.items():
    if count > max_count:
        max_count = count
        mode = num

print(f"Mode: {mode} (occurs {max_count} times)")