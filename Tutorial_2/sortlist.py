n = int(input("Enter the number of names: "))
names = []

for i in range(n):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

for i in range(len(names)):
    for j in range(0, len(names) - i - 1):
        if names[j] > names[j + 1]:
            names[j], names[j + 1] = names[j + 1], names[j]

print("Sorted names:")
for name in names:
    print(name)