n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    num = input(f"Enter element {i+1}: ")
    numbers.append(num)

unique_list = []
for item in numbers:
    if item not in unique_list:
        unique_list.append(item)

print("List after removing duplicates:", unique_list)