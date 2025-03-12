def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

print("Numbers between 100 and 1000 whose sum of digits is divisible by 9:")
for num in range(100, 1001):
    if sum_of_digits(num) % 9 == 0:
        print(num, end=" ")