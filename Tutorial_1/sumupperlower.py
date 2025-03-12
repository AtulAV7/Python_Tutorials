def sum_of_odd_numbers(lower, upper):
    if lower % 2 == 0:
        lower += 1
    
    total = 0
    for num in range(lower, upper+1, 2):  
        total += num
    
    return total

lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

result = sum_of_odd_numbers(lower, upper)
print(f"Sum of odd numbers between {lower} and {upper} is {result}")