
# Name:                 Random Password Generator
# Purpose:              Advance Python Class
# Author:               Muzaffar Ali
# Version:              1.0
# Copyright:            (c) Muzaffar Ali
# License:              Public
# Requirements-1:       Random: The random module provides functions that generate random numbers and selections, 
#                       which are essential for creating unpredictable passwords
# Requirements-2:       String: The string module provides a collection of string constants which are useful for various text operations.




import random
import string

def generate_password(length):
    if length < 4:  # Ensure the minimum length to include all character types
        raise ValueError("Password length should be at least 4 to include all character types.")

    # Define the characters to use in the password
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    # Ensure the password contains at least one character from each category
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_chars),
        random.choice(letters + digits + special_chars)
    ]

    # Fill the rest of the password length with random choices from all characters
    if length > 4:
        password += random.choices(letters + digits + special_chars, k=length-4)

    # Shuffle the result to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

# Set the desired password length
password_length = 20

# Generate and print the password
print("Generated Password:", generate_password(password_length))

