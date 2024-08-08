
# Name:                 Print characters from string that are present at an even index number (Muzaffar Ali)
# Purpose:              Advance Python Class
# Author:               Muzaffar Ali
# Version:              1.0
# Created:              31/07/2024
# Copyright:            (c) Muzaffar Ali
# License:              Public


# Exercise 3: Print characters from string that are present at an even index number

word = input("Enter a word: ")

print("Exercise 3: Print characters from string that are present at an even index number")

# Taking the Length fo variable "word" and for even word.
for i in range(len(word)):
    if i % 2 == 0:
        print(word[i])
