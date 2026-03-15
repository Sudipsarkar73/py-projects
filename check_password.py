def check_password_strength(password):
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    special_count = 0
    
    min_length = 8

    if len(password) < min_length:
        print(f" Weak: Password is too short (must be at least {min_length} characters).")
        return

    for char in password:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            special_count += 1

    if uppercase_count>0 and lowercase_count>0 and digit_count>0 and special_count>0:
        print("strong password")
    else:
        print("weak password")
    print("Uppercase count =",uppercase_count)
    print("Lowercase count=",lowercase_count)
    print("Digit count =",digit_count)
    print("Special character count =",special_count)

user_password = input("Enter a password to check its strength: ")
check_password_strength(user_password)

