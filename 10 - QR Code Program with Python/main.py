
# Name:                 QR Code Program with Python
# Purpose:              Advance Python Class
# Author:               Muzaffar Ali
# Version:              1.0
# Copyright:            (c) Muzaffar Ali
# License:              Public
# Requirements-1:       pyqrcode: Imports the QRCode class from the pyqrcode module.


import pyqrcode
from pyqrcode import QRCode

# Prompt the user to enter a URL to encode into the QR Code
Content = input("Enter your URL: ")

# Generate QR Code from the provided URL
url = pyqrcode.create(Content)

# Prompt the user to enter the desired file name for the QR Code
file_name = input("Enter your file name: ")
# Append the .svg extension to the file name
file_name = file_name + ".svg"

# Create and save the QR Code as an SVG file with the specified file name
url.svg(file_name, scale=8)

# Print the QR Code to the terminal in a readable format
print(url.terminal(quiet_zone=1))
