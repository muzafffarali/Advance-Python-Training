
# Name:                 Encode Caesar Cipher with Username and Password (Decode)
# Purpose:              Advance Python Class
# Author:               Muzaffar Ali
# Version:              1.0
# Copyright:            (c) Muzaffar Ali
# License:              Public
# Requirements-1:       pyzbar: Imports the decode function from the pyzbar.pyzbar module to decode QR codes.
# Requirements-2:       Pillow: Imports the Image class from the PIL (Pillow) library to handle image operations.
# Requirements-3:       String: Imports the string module to access predefined character sets.



from pyzbar.pyzbar import decode
from PIL import Image
import string

def get_pin():
    """
    Prompt the user to enter a PIN between 0 and 100. Validate the input and return the PIN.
    """
    while True:
        try:
            pin = int(input("Put your private PIN (0-100): "))
            if 0 <= pin <= 100:
                return pin
            else:
                print("PIN must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 100.")

def reverse_caesar_cipher(cipher_message, shift):
    """
    Decipher the given message using a reverse Caesar cipher with the specified shift.
    
    Parameters:
    cipher_message (str): The ciphered message to decipher.
    shift (int): The number of positions to shift each character in the reverse direction.
    
    Returns:
    str: The original, deciphered message.
    """
    Charset = string.ascii_letters + string.digits + "!@#$%^&*()"
    original_message = []
    
    for char in cipher_message:
        if char in Charset:
            idx = Charset.index(char)
            original_idx = (idx - shift) % len(Charset)
            original_message.append(Charset[original_idx])
        else:
            original_message.append(char)
    
    return "".join(original_message)

def decode_qr_code(Image_path):
    """
    Decode the QR code in the specified image file.
    
    Parameters:
    Image_path (str): The path to the image file containing the QR code.
    
    Returns:
    str: The decoded data from the QR code, or None if no QR code is found.
    """
    img = Image.open(Image_path)
    decoded_objects = decode(img)
    if decoded_objects:
        return decoded_objects[0].data.decode("utf-8")
    else:
        return None

def main():
    """
    Main function to decode a QR code, get a PIN from the user, and decipher the message.
    """
    Image_path = input("Enter the path to the QR code image file: ")
    cipher_message = decode_qr_code(Image_path)
    if cipher_message:
        print(f"Ciphered message from QR code: {cipher_message}")
        
        pin = get_pin()
        original_message = reverse_caesar_cipher(cipher_message, pin)
        print(f"Original message: {original_message}")
    else:
        print("No QR code found in the image.")

if __name__ == "__main__":
    main()