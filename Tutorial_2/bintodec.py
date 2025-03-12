binary = input("Enter a binary number: ")
decimal = 0
power = 0

for digit in binary[::-1]:  
    if digit == '1':
        decimal = decimal + 2 ** power
    power = power + 1

print("Decimal representation:", decimal)