def calculate_stats(numbers):
    positive_sum = 0
    negative_sum = 0
    positive_count = 0
    negative_count = 0
    
    for num in numbers:
        if num > 0:
            positive_sum += num
            positive_count += 1
        elif num < 0:
            negative_sum += num
            negative_count += 1
    
    positive_avg = positive_sum / positive_count if positive_count > 0 else 0
    negative_avg = negative_sum / negative_count if negative_count > 0 else 0
    
    return positive_sum, negative_sum, positive_avg, negative_avg

numbers = []
for i in range(4):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)

pos_sum, neg_sum, pos_avg, neg_avg = calculate_stats(numbers)
print(f"Sum of positive numbers: {pos_sum}")
print(f"Sum of negative numbers: {neg_sum}")
print(f"Average of positive numbers: {pos_avg}")
print(f"Average of negative numbers: {neg_avg}")