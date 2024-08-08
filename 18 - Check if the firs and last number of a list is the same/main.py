
# Name:                 Check if the firs and last number of a list is the same
# Purpose:              Advance Python Class
# Author:               Muzaffar Ali
# Version:              1.0
# Created:              31/07/2024
# Copyright:            (c) Muzaffar Ali
# License:              Public


# Check if the firs and last number of a list is the same

def sameList(numlist):
    return numlist[0] == numlist[-1]

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print("Given list: ", numbers)
print("Result list: ", sameList(numbers))