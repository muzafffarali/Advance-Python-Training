
# Name:                 Random Password Generator
# Purpose:              Advance Python Class
# Author:               Muzaffar Ali
# Version:              1.0
# Copyright:            (c) Muzaffar Ali
# License:              Public
# Requirements-1:       time : The time library provides various time-related functions. In this code, it is used to get the current local time.
# Requirements-2:       calendar : The calendar library provides functions related to calendar operations. In this code, it is used to check if a year is a leap year.


import time
from calendar import isleap

# Function to judge if a year is a leap year
def judgeLeapYear(year):
    return isleap(year)

# Function to return the number of days in each month
def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if leap_year else 28

# Getting user input
name = input("What is your name?: \n")
while True:
    try:
        age = int(input("What is your age?: \n"))
        break
    except ValueError:
        print("Please enter a valid age.")

# Get the current local time
localtime = time.localtime(time.time())
years = age
months = years * 12 + localtime.tm_mon
days = 0

# Calculate the start and end year
begin_year = localtime.tm_year - years
end_year = begin_year + years

# Calculate the total number of days lived
for y in range(begin_year, end_year):
    days += 366 if judgeLeapYear(y) else 365

# Determine if the current year is a leap year
leap_year = judgeLeapYear(localtime.tm_year)

# Calculate the days lived in the current year up to the current month
for m in range(1, localtime.tm_mon):
    days += month_days(m, leap_year)

# Add the current day of the month
days += localtime.tm_mday

# Print the result
print(f"{name}'s age is {years} years or {months} months or {days} days.")
