input_string = input("Enter a string: ")
mid = len(input_string) // 2

first_half = input_string[:mid]
second_half = input_string[mid:]

reversed_first = ""
for i in range(len(first_half)-1, -1, -1):
    reversed_first = reversed_first + first_half[i]

reversed_second = ""
for i in range(len(second_half)-1, -1, -1):
    reversed_second = reversed_second + second_half[i]

result = reversed_first + reversed_second
print("String after reversing halves:", result)