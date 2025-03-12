input_string = input("Enter a string: ")
words_to_remove = input("Enter words to remove (separated by space): ").split()

words = input_string.split()
result = []

for word in words:
    if word not in words_to_remove:
        result.append(word)

output_string = " ".join(result)
print("String after removing words:", output_string)