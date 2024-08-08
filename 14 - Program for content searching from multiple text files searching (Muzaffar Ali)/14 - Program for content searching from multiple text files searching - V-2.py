
# Name:                 Program for content searching from multiple text files searching - V-2
# Purpose:              Advance Python Class
# Author:               Muzaffar Ali
# Version:              1.0
# Created:              31/07/2024
# Copyright:            (c) Muzaffar Ali
# License:              Public
# Requirements-1:       imports the OS MODULE, which provides functions for interacting with the 
#                       operating system, such as reading or writing files and directories.

import os

def getfiles(path, keyword):
    """
    Recursively searches for files containing a specific keyword within a given directory.

    Parameters:
    path (str): The directory path to search.
    keyword (str): The keyword to search for in files.

    Returns:
    list: A list of file paths that contain the keyword.
    """
    found_files = []
    
    try:
        # List all files and directories in the given path
        files = os.listdir(path)
    except OSError as e:
        # Handle errors if the directory cannot be accessed
        print(f"Error accessing {path}: {e}")
        return found_files
    
    for filename in files:
        # Get the absolute path of the file/directory
        abs_path = os.path.join(path, filename)
        
        if os.path.isdir(abs_path):
            # Recursively search in subdirectories
            found_files.extend(getfiles(abs_path, keyword))
        elif os.path.isfile(abs_path):
            try:
                # Open and read the file
                with open(abs_path, "r", encoding="utf-8", errors="ignore") as f:
                    # If the keyword is found in the file, add the file path to the list
                    if keyword in f.read():
                        found_files.append(abs_path)
            except (OSError, IOError) as e:
                # Handle errors if the file cannot be read
                print(f"Error reading file {abs_path}: {e}")
    
    return found_files

if __name__ == "__main__":
    # Get keyword and directory path from user
    keyword = input("Keyword: ")
    path = input("Location: ")
    
    if not os.path.isdir(path):
        # Validate if the given path is a directory
        print(f"The path {path} is not a valid directory.")
    else:
        # Search for files containing the keyword
        found_files = getfiles(path, keyword)
        if not found_files:
            # If no files are found, print a message
            print(f"'{keyword}' not found in the location.")
        else:
            # If files are found, print their paths
            print(f"'{keyword}' found in the following files:")
            for file_path in found_files:
                print(file_path)
