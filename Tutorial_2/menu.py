def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

def check_sign(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def generate_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

while True:
    print("\nMenu:")
    print("1. Check if a number is even or odd")
    print("2. Check if a number is positive, negative, or zero")
    print("3. Generate factors of a number")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '4':
        print("Exiting program...")
        break
    
    num = int(input("Enter a number: "))
    
    if choice == '1':
        result = check_even_odd(num)
        print(f"{num} is {result}")
    elif choice == '2':
        result = check_sign(num)
        print(f"{num} is {result}")
    elif choice == '3':
        factors = generate_factors(num)
        print(f"Factors of {num}: {factors}")
    else:
        print("Invalid choice! Please try again.")