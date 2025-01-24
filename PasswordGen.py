import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")
    
    # Use SystemRandom for better randomness
    secure_random = random.SystemRandom()

    # Define character pools
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation
    all_characters = upper + lower + digits + special

    # Ensure at least one character from each pool
    password = [
        secure_random.choice(upper),
        secure_random.choice(lower),
        secure_random.choice(digits),
        secure_random.choice(special)
    ]

    # Fill the rest of the password length with random characters
    password += [secure_random.choice(all_characters) for _ in range(length - 4)]

    # Shuffle the password to avoid predictable patterns
    secure_random.shuffle(password)

    return ''.join(password)

# Get user input for password length
try:
    password_length = int(input("Enter the desired password length (minimum 4): "))
    print("Generated Password:", generate_password(password_length))
except ValueError as e:
    print("Error:", e)
