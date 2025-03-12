input_string = input("Enter a string: ")
result = ""

for char in input_string:
    if 'a' <= char <= 'z':
        result = result + chr(ord(char) - 32)
    else:
        result = result + char

print("Uppercase string:", result)