decimal = int(input("Enter a decimal number: "))
binary = ""

if decimal == 0:
    binary = "0"
else:
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2

print("Binary representation:", binary)