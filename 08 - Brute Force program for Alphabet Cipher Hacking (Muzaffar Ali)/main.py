
# Name:                 08 - Brute Force program for Alphabet Cipher Hacking
# Purpose:              Advance Python Class
# Author:               Muzaffar Ali
# Version:              1.0
# Copyright:            (c) Muzaffar Ali
# License:              Public


# Create an alphabet list containing 'a' to 'z', repeated four times
alphabet = [chr(i) for i in range(97, 123)] * 4

def caesar(start_text, shift_amount, cipher_direction):
    """
    This function encodes or decodes the given text using the Caesar cipher.
    
    Parameters:
    start_text (str): The text to encode or decode.
    shift_amount (int): The number of positions to shift each character.
    cipher_direction (str): Either 'encode' to encrypt or 'decode' to decrypt.
    
    Returns:
    str: The encoded or decoded text.
    """
    end_text = ""
    if cipher_direction == "decode":
        # Reverse the shift amount for decoding
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            # Find the current position of the character
            position = alphabet.index(char)
            # Calculate the new position after shifting
            new_position = position + shift_amount
            # Append the new character to the result text
            end_text += alphabet[new_position]
        else:
            # If the character is not in the alphabet, leave it unchanged
            end_text += char
    return end_text

def brute_force_caesar(cipher_text):
    """
    This function attempts to decode the given cipher text using all possible shift amounts (0-99).
    
    Parameters:
    cipher_text (str): The text to decode.
    """
    print("Brute Force Results:")
    for shift in range(100):
        # Decode the text with the current shift amount
        decoded_text = caesar(start_text=cipher_text, shift_amount=shift, cipher_direction="decode")
        # Print the result for the current shift amount
        print(f"Shift amount {shift}: {decoded_text}")

# Get the cipher text from the user
cipher_text = input("Enter the cipher text to brute force:\n").lower()
# Perform brute force decoding on the input cipher text
brute_force_caesar(cipher_text)
