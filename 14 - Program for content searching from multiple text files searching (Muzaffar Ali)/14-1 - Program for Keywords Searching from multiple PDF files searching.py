
# Name:                 Program for Keywords Searching from multiple PDF files searching
# Purpose:              Advance Python Class
# Author:               Muzaffar Ali
# Version:              1.0
# Created:              31/07/2024
# Copyright:            (c) Muzaffar Ali
# License:              Public
# Requirements-1:       imports the OS MODULE, which provides functions for interacting with the 
#                       operating system, such as reading or writing files and directories.
# Requirements-2:       imports the PdfReader class from the PyPDF2 library, which is used to read PDF files.


import os
from PyPDF2 import PdfReader

def get_pdf_files(directory):
    """
    This function takes a directory path and returns a list of all PDF files in that directory.
    """
    # List all files in the directory and filter out only the PDF files
    pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]
    return pdf_files

def search_keywords_in_pdf(file_path, keywords):
    """
    This function searches for multiple keywords in a given PDF file.
    It returns a dictionary where each keyword maps to a list of pages where it is found
    and the total count of keyword occurrences.
    """
    results = {keyword: {'pages': [], 'count': 0} for keyword in keywords}  # Initialize result dictionary
    reader = PdfReader(file_path)  # Open the PDF file using PdfReader
    num_pages = len(reader.pages)  # Get the number of pages in the PDF file

    # Loop through each page in the PDF
    for page_num in range(num_pages):
        page_text = reader.pages[page_num].extract_text()  # Extract text from the current page
        for keyword in keywords:
            if keyword.lower() in page_text.lower():  # Check if the keyword is in the page text (case-insensitive)
                results[keyword]['pages'].append(page_num + 1)  # Add the page number (1-indexed) to the list
                results[keyword]['count'] += page_text.lower().count(keyword.lower())  # Count occurrences of the keyword

    return results  # Return the results dictionary

def main():
    """
    Main function to execute the script.
    """
    # Loop until a valid directory path is provided
    while True:
        # Prompt the user to enter the directory path containing the PDF files
        directory = input("Please enter the directory path containing the PDF files: ")

        # Check if the provided directory exists
        if os.path.isdir(directory):
            break
        else:
            print("Error: The provided directory does not exist. Please try again.")

    # Get the list of PDF files in the directory
    pdf_files = get_pdf_files(directory)
    
    # Check if there are no PDF files in the directory
    if not pdf_files:
        print("Error: No PDF files found in the provided directory.")
        return

    # Print the number of accessed PDF files
    print(f"Accessed {len(pdf_files)} PDF files.")

    while True:
        # Prompt the user to enter the keywords to search for, separated by commas
        keywords_input = input("Please enter the keywords to search for (separated by commas): ")
        keywords = [keyword.strip() for keyword in keywords_input.split(",")]

        if not keywords or all(keyword == "" for keyword in keywords):
            print("Error: You must enter at least one keyword.")
            return

        grand_total_counts = {keyword: 0 for keyword in keywords}  # Initialize grand total counts for each keyword

        # Loop through each PDF file and search for the keywords
        for pdf_file in pdf_files:
            file_path = os.path.join(directory, pdf_file)  # Construct the full file path
            try:
                # Search for the keywords in the current PDF file
                results = search_keywords_in_pdf(file_path, keywords)
                for keyword, data in results.items():
                    grand_total_counts[keyword] += data['count']  # Add to the grand total count
                    if data['pages']:
                        # Print the results if the keyword is found
                        print(f"In file '{pdf_file}':")
                        print(f"The keyword '{keyword}' is found on pages: {data['pages']}")
                        print(f"Total occurrences of the keyword '{keyword}': {data['count']}\n")
                    else:
                        # Print a message if the keyword is not found
                        print(f"The keyword '{keyword}' is not found in file '{pdf_file}'.\n")
            except Exception as e:
                # Print an error message if there is an issue processing the file
                print(f"Error processing file '{pdf_file}': {e}")

        # Print the grand total occurrences of each keyword
        for keyword, total_count in grand_total_counts.items():
            print(f"Grand total occurrences of the keyword '{keyword}': {total_count}")

        # Ask the user if they want to search for more keywords
        search_again = input("Do you want to search for more keywords? Type 'y' for yes, 'n' for no: ").strip().lower()
        if search_again != 'y':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()  # Call the main function to execute the script
