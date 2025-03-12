input_string = input("Enter a string: ")
result = ""

for char in input_string:
    if char.lower() not in "aeiou":
        result = result + char

print("String after removing vowels:", result)