input_string = input("Enter a string: ")
result = ""
space_found = False

for char in input_string:
    if char == " ":
        result = result + "*"
        space_found = True
    else:
        result = result + char

if not space_found:
    result = "$" + result + "$"

print("Modified string:", result)