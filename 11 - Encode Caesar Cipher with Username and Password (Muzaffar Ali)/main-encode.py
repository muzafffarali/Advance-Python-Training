
# Name:                 Encode Caesar Cipher with Username and Password (encode)
# Purpose:              Advance Python Class
# Author:               Muzaffar Ali
# Version:              1.0
# Copyright:            (c) Muzaffar Ali
# License:              Public
# Requirements-1:       getpass: Provides a secure way to handle password input.
# Requirements-2:       qrcode: A module to generate QR codes.
# Requirements-3:       string: Provides a collection of string constants, such as ASCII letters and digits.



import getpass
import qrcode
import string

# Authentication details
USERNAME = "admin"
PASSWORD = "1234"

def authenticate():
    """
    Prompt the user for a username and password. Return True if they match the stored credentials, False otherwise.
    """
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    return username == USERNAME and password == PASSWORD

def get_message():
    """
    Prompt the user to enter a message. Ensure the message is between 1 and 1000 characters long.
    """
    while True:
        msg = input("What is your message: ")
        if 1 <= len(msg) <= 1000:
            return msg
        else:
            print("Message must be between 1 and 1000 characters.")
            
def get_pin():
    """
    Prompt the user to enter a private PIN between 0 and 100. Validate the input to ensure it is a number within the range.
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
            
def caesar_cipher(message, shift):
    """
    Apply a Caesar cipher to the given message with the specified shift.
    
    Parameters:
    message (str): The message to be ciphered.
    shift (int): The number of positions to shift each character.
    
    Returns:
    str: The ciphered message.
    """
    Charset = string.ascii_letters + string.digits + "!@#$%^&*()"
    shifted_message = []
    
    for char in message:
        if char in Charset:
            idx = Charset.index(char)
            shifted_idx = (idx + shift) % len(Charset)
            shifted_message.append(Charset[shifted_idx])
        else:
            shifted_message.append(char)
    
    return "".join(shifted_message)

def generate_qr_code(data):
    """
    Generate a QR code from the given data and save it as 'cipher_message_qr.png'.
    
    Parameters:
    data (str): The data to encode in the QR code.
    """
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save("cipher_message_qr.png")
    print("QR code saved as 'cipher_message_qr.png'")
    
def main():
    """
    Main function to handle the workflow: authenticate, get message, get PIN, cipher the message, and generate a QR code.
    """
    while not authenticate():
        print("Authentication failed. Please try again.")
    message = get_message()
    pin = get_pin()
    cipher_message = caesar_cipher(message, pin)
    print(f"Ciphered message: {cipher_message}")
    generate_qr_code(cipher_message)

if __name__ == "__main__":
    main()
