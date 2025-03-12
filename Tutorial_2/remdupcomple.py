n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    num = input(f"Enter element {i+1}: ")
    numbers.append(num)

counts = {}
for item in numbers:
    if item in counts:
        counts[item] = counts[item] + 1
    else:
        counts[item] = 1

result = []
for item in numbers:
    if counts[item] == 1:
        result.append(item)

print("List after removing all duplicates completely:", result)