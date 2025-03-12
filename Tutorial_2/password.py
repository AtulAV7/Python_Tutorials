password = input("Enter your password: ")

has_lowercase = False
has_uppercase = False
has_digit = False
has_special = False
valid_length = len(password) >= 6

for char in password:
    if 'a' <= char <= 'z':
        has_lowercase = True
    elif 'A' <= char <= 'Z':
        has_uppercase = True
    elif '0' <= char <= '9':
        has_digit = True
    elif char in '$#@':
        has_special = True

if has_lowercase and has_uppercase and has_digit and has_special and valid_length:
    print("Password is valid")
else:
    print("Password is invalid")
    if not has_lowercase:
        print("- Missing lowercase letter")
    if not has_uppercase:
        print("- Missing uppercase letter")
    if not has_digit:
        print("- Missing digit")
    if not has_special:
        print("- Missing special character ($, #, @)")
    if not valid_length:
        print("- Password length should be at least 6 characters")