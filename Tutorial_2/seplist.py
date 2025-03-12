n = int(input("Enter the number of elements: "))
mixed_list = []

for i in range(n):
    item = input(f"Enter element {i+1} (use quotes for strings): ")
    
    try:
        int_val = int(item)
        mixed_list.append(int_val)
    except ValueError:
        try:
            float_val = float(item)
            mixed_list.append(float_val)
        except ValueError:
            mixed_list.append(item)

integers = []
floats = []
strings = []

for item in mixed_list:
    if type(item) == int:
        integers.append(item)
    elif type(item) == float:
        floats.append(item)
    else:
        strings.append(item)

print("Integers:", integers)
print("Floats:", floats)
print("Strings:", strings)