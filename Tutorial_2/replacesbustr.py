main_string = input("Enter the main string: ")
old_substring = input("Enter the substring to replace: ")
new_substring = input("Enter the new substring: ")

result = ""
i = 0

while i < len(main_string):
    if main_string[i:i+len(old_substring)] == old_substring:
        result = result + new_substring
        i = i + len(old_substring)
    else:
        result = result + main_string[i]
        i = i + 1

print("String after replacement:", result)