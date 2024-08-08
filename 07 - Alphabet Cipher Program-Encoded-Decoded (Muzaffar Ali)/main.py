
# Name:                 07 - Alphabet Cipher Program-Encoded-Decoded
# Purpose:              Advance Python Class
# Author:               Muzaffar Ali
# Version:              1.0
# Copyright:            (c) Muzaffar Ali
# License:              Public


# Alphabet list repeated to handle wrapping around when shifting characters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    # If decoding, reverse the shift amount
    if cipher_direction == "decode":
        shift_amount *= -1
    # Iterate through each character in the input text
    for char in start_text:
        # Check if the character is in the alphabet list
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
    # Print the final encoded or decoded text
    print(f"Here's the {cipher_direction}d result: {end_text}")

should_end = False
while not should_end:
    # Ask the user for the direction: encode or decode
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # Ask the user for the text to encode or decode
    text = input("Type your message:\n").lower()
    # Ask the user for the shift amount
    shift = int(input("Type the shift number:\n"))

    # Ensure the shift amount is within the range of 0-25
    shift = shift % 26

    # Call the caesar function with the user inputs
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # Ask the user if they want to go again
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
