
# Name:                 BMI Calculator Program
# Purpose:              Advance Python Class
# Author:               Muzaffar Ali
# Version:              1.0
# Copyright:            (c) Muzaffar Ali
# License:              Public


# Prompt the user to enter their height in centimeters and convert it to a float
height = float(input("Enter the Height in CM: "))

# Prompt the user to enter their weight in kilograms and convert it to a float
weight = float(input("Enter the Weight in Kilograms: "))

# Convert height from centimeters to meters
Height = height / 100

# Calculate BMI using the formula weight / (height in meters * height in meters)
BMI = weight / (Height * Height)

# Print the calculated BMI
print("Your body mass:", BMI)

# Check the BMI value and print the corresponding weight category
if BMI <= 16:
    print("Severely underweight")
elif BMI <= 18.5:
    print("Underweight")
elif BMI <= 25:
    print("Normal weight")
elif BMI <= 30:
    print("Overweight")
else:
    print("Severely overweight")
