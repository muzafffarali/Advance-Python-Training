

# Name:                 Encode Caesar Cipher with Username and Password (Encode & Decode)
# Purpose:              Advance Python Class
# Author:               Muzaffar Ali
# Version:              1.0
# Copyright:            (c) Muzaffar Ali
# License:              Public
# Requirements-1:       pyqrcode: To create QR codes.
# Requirements-2:       QRCode: To handle QR code generation.
# Requirements-3:       PIL.Image: To handle image operations.
# Requirements-4:       pyzbar.pyzbar.decode: To decode QR codes
# Requirements-5:       os: To handle file paths.
# Requirements-6:       string: To access printable characters.


import pyqrcode
from pyqrcode import QRCode
from PIL import Image
from pyzbar.pyzbar import decode
import os
import string

# Default credentials for authentication
DEFAULT_USERNAME = "admin"
DEFAULT_PASSWORD = "password"

# Function to authenticate user
def authenticate():
    username = input("Username: ")
    password = input("Password: ")
    if username == DEFAULT_USERNAME and password == DEFAULT_PASSWORD:
        return True
    else:
        print("Authentication failed!")
        return False

# Function to validate message input
def validate_message(message):
    # Check if the message length is between 1 and 100 and contains only printable characters
    if 1 <= len(message) <= 100 and all(c in string.printable for c in message):
        return True
    return False

# Function to validate PIN
def validate_pin(pin):
    # Check if the PIN is between 0 and 100
    return 0 <= pin <= 100

# Function for Caesar cipher
def caesar_cipher(text, shift, encode=True):
    # Define the set of characters that can be shifted
    characters = string.printable
    # Reverse the shift amount for decoding
    if not encode:
        shift = -shift
    translated = []
    for char in text:
        if char in characters:
            # Find the index of the character and apply the shift
            idx = characters.index(char)
            new_idx = (idx + shift) % len(characters)
            translated.append(characters[new_idx])
        else:
            # If the character is not in the set, add it unchanged
            translated.append(char)
    return ''.join(translated)

# Function to generate QR code
def generate_qr_code(content, file_path):
    try:
        # Create and save the QR code
        url = pyqrcode.create(content)
        url.png(file_path, scale=8)
        print(f"QR code generated and saved at {file_path}")
    except Exception as e:
        print(f"Error generating QR code: {e}")

# Function to read QR code
def read_qr_code(file_path):
    try:
        # Open the image and decode the QR code
        decoded_objects = decode(Image.open(file_path))
        for obj in decoded_objects:
            # Return the decoded data
            return obj.data.decode('utf-8')
        return None
    except Exception as e:
        print(f"Error reading QR code: {e}")
        return None

# Main program
def main():
    if not authenticate():
        print("Access denied!")
        return

    # Prompt for and validate PIN
    pin = int(input("Put your private PIN (0-100): "))
    while not validate_pin(pin):
        print("Invalid PIN! Please enter a valid PIN (0-100).")
        pin = int(input("Put your private PIN (0-100): "))

    # Ask for the operation direction
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    
    if direction == "encode":
        # Validate message
        message = input("What is your message (max 100 characters, allowed charset printable ASCII): ")
        while not validate_message(message):
            print("Invalid message! Please enter a valid message.")
            message = input("What is your message (max 100 characters, allowed charset printable ASCII): ")
        
        # Perform Caesar cipher to encode the message
        shift = pin % len(string.printable)
        cipher_text = caesar_cipher(message, shift, encode=True)
        print(f"Here's the encoded result: {cipher_text}")

        # Get file location and name for QR code
        file_location = input("Enter the directory to save the QR code (e.g., C:/Users/YourName/Desktop): ")
        file_name = input("Enter the file name for the QR code (without extension): ") + ".png"
        file_path = os.path.join(file_location, file_name)
        
        # Generate QR code
        generate_qr_code(cipher_text, file_path)
    
    elif direction == "decode":
        # Get file location and name of the QR code to decode
        file_location = input("Enter the directory of the QR code image (e.g., C:/Users/YourName/Desktop): ")
        file_name = input("Enter the QR code file name to decode (without extension): ") + ".png"
        file_path = os.path.join(file_location, file_name)

        # Read QR code
        cipher_text = read_qr_code(file_path)
        if cipher_text:
            # Perform Caesar cipher to decode the message
            shift = pin % len(string.printable)
            decoded_text = caesar_cipher(cipher_text, shift, encode=False)
            print(f"Here's the decoded result: {decoded_text}")
        else:
            print("Failed to read QR code.")

if __name__ == "__main__":
    main()
