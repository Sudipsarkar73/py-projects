import string
import random

def generate_password(length):

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    all_chars = lower + upper + digits + symbols

    if length < 8:
        print("Minimum length of 8 is required. Setting length to 8.")
        length = 8 

    required_chars = [
        random.choice(lower),       
        random.choice(upper),    
        random.choice(symbols),    
        random.choice(digits)      
    ]
    
    remaining_length = length - len(required_chars)
    
    remaining_chars = []
    for i in range(remaining_length):
        random_char = random.choice(all_chars)
        remaining_chars.append(random_char)
    
    password_list = required_chars + remaining_chars
    random.shuffle(password_list)

    print("".join(password_list))
    """ return "".join(password_list)"""

length= int(input("Enter length of pass: "))
generate_password(length)

