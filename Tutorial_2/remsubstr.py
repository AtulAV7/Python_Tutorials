main_string = input("Enter the main string: ")
substring = input("Enter the substring to remove: ")

result = ""
i = 0

while i < len(main_string):
    if main_string[i:i+len(substring)] == substring:
        i = i + len(substring)
    else:
        result = result + main_string[i]
        i = i + 1

print("String after removing substring:", result)