input_string = input("Enter a string: ")
even_chars = ""
odd_chars = ""

for i in range(len(input_string)):
    if i % 2 == 0:
        even_chars = even_chars + input_string[i]
    else:
        odd_chars = odd_chars + input_string[i]

print("Characters at even indices:", even_chars)
print("Characters at odd indices:", odd_chars)