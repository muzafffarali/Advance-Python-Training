
# Name:                 Excel Filtration Toll in Python - V-1
# Purpose:              Advance Python Class
# Author:               Muzaffar Ali
# Version:              1.0
# Created:              31/07/2024
# Copyright:            (c) Muzaffar Ali
# License:              Public
# Requirements-1:       The script uses the pandas library to read an Excel file and search for a specific value in a specified column. 


import pandas as pd  # Library for reading excel file

# Function to search for a value in a specific column of an Excel sheet
def search_excel(file_path, sheet_name, search_column, search_value):
    # Read the Excel file and specified sheet into a DataFrame
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    # Search for rows where the value in the specified column matches the search value
    search_result = df[df[search_column] == search_value]
    
    # Check if the search result is not empty and return the result
    if not search_result.empty:
        return search_result
    else:
        # Return a message if no matching records are found
        return "No matching records found."

# Define the file path, sheet name, column to search, and the value to search for
file_path = "data.xlsx"
sheet_name = "Sheet1"
search_column = "Category"
search_value = "Shirt"

# Call the search function and store the result
result = search_excel(file_path, sheet_name, search_column, search_value)

# Print the result
print(result)
