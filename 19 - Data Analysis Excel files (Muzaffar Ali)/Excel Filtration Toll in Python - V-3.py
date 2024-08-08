
# Name:                 Excel Filtration Toll in Python - V-3
# Purpose:              Advance Python Class
# Author:               Muzaffar Ali
# Version:              1.0
# Created:              31/07/2024
# Copyright:            (c) Muzaffar Ali
# License:              Public
# Requirements-1:       The script uses the pandas library to read an Excel file and search for a specific value in a specified column. 


import pandas as pd  # Library for reading Excel file

def search_and_save_excel(input_file, search_column_index, search_value, output_file):
    """
    Searches for a value in a specified column of an Excel file and saves the search results to a new Excel file.

    Parameters:
    input_file (str): Path to the input Excel file.
    search_column_index (int): Index of the column to search.
    search_value (str): Value to search for in the specified column.
    output_file (str): Path to save the search results.

    Returns:
    str: A message indicating the result of the operation.
    """
    # Read the input Excel file into a DataFrame
    df = pd.read_excel(input_file)

    # Check if the search column index is valid
    if search_column_index < 0 or search_column_index >= len(df.columns):
        return f"Invalid search column index: {search_column_index}"

    # Get the column name using the index
    search_column = df.columns[search_column_index]

    # Perform the search operation
    # Convert the column to string and check if it contains the search value (case insensitive)
    search_results = df[df[search_column].astype(str).str.contains(str(search_value), case=False)]

    # Save the search results to the output Excel file
    search_results.to_excel(output_file, index=False)

    # Return a success message
    return f"Search results saved to {output_file}"

# Define the input file path
input_file = 'data.xlsx'

# Prompt the user to enter the column index and search value
search_column_index = int(input("Please enter the Column Index No: "))
search_value = input("Please enter the Keyword you want to search: ")

# Define the output file path
output_file = 'Searching_Results_1.xlsx'

# Call the function and store the result message
result_message = search_and_save_excel(input_file, search_column_index, search_value, output_file)

# Print the result message
print(result_message)
