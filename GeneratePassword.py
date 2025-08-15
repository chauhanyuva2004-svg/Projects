import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4."
    
    # Characters: letters, digits, symbols
    all_chars = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# Get length from user
try:
    length = int(input("Enter password length: "))
    print("Generated Password:", generate_password(length))
except ValueError:
    print("Please enter a valid number.")
