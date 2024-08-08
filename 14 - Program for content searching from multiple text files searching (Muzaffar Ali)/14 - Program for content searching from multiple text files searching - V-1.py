
# Name:                 Program for content searching from multiple text files searching - V-1
# Purpose:              Advance Python Class
# Author:               Muzaffar Ali
# Version:              1.0
# Created:              31/07/2024
# Copyright:            (c) Muzaffar Ali
# License:              Public
# Requirements-1:       imports the OS MODULE, which provides functions for interacting with the 
#                       operating system, such as reading or writing files and directories.

import os
text = input("Keyword: ")
path = input("Location: ")


def getfiles(path):
    """
    This line defines a new function named getfiles that takes one parameter, path, 
    which represents the directory path.
    """
    f = 0 # This initializes a variable f to 0. This variable will be used as a flag to indicate if the keyword is found
    os.chdir(path) # This changes the current working directory to the path provided by the user.
    files = os.listdir() # This gets a list of all files and directories in the current working directory and stores it in the variable files.
    
    for file_name in files: # This starts a loop that iterates over each item (file or directory) in files.
        abs_path = os.path.abspath(file_name) # This gets the absolute path of the current file or directory.
        if os.path.isdir(abs_path): # This checks if the current item is a directory
            getfiles(abs_path) # If it is a directory, the function calls itself recursively with the new directory path. This is known as recursion and helps to traverse all subdirectories
        if os.path.isfile(abs_path): # This checks if the current item is a file
            f = open(file_name, "r") # If it is a file, it opens the file in read mode.
            if text in f.read(): # This reads the file content and checks if the keyword (text) is in the file.
                f = 1 # If the keyword is found, it sets f to 1.
                print(text + " found in ") # It prints a message indicating the keyword was found.
                final_path = os.path.abspath(file_name) # It gets the absolute path of the file where the keyword was found.
                print(final_path) # It prints the absolute path of the file.
                return True # It returns True indicating the keyword was found and stops further execution of the function.
    if f ==1: # This checks if the flag f is set to 1, indicating the keyword was found
        print(text + " Not found! ") # If f is not 1, it prints a message indicating the keyword was not found.
        return False # It returns False indicating the keyword was not found.
getfiles(path) # This line calls the getfiles function with the user-provided path as the argument, starting the process of searching for the keyword in the specified directory and its subdirectories
