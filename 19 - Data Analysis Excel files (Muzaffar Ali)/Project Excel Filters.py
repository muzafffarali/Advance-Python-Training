
# Name:                 Project Excel Filters
# Purpose:              Advance Python Class
# Author:               Muzaffar Ali
# Version:              1.0
# Created:              31/07/2024
# Copyright:            (c) Muzaffar Ali
# License:              Public
# Requirements-1:       pandas: Used for data manipulation and analysis, providing powerful data structures like DataFrames and Series.
# Requirements-2:       os: Provides a way to interact with the operating system, handling file and directory operations.
# Requirements-3:       matplotlib.pyplot Used for creating visualizations, including various types of plots and charts.



import pandas as pd  # Library for reading and manipulating Excel files
import os  # Library for file path operations
import matplotlib.pyplot as plt  # Library for data visualization

def load_excel(file_path):
    """
    Load an Excel file.

    Args:
        file_path (str): The path to the Excel file.

    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    try:
        # Check if the file exists and is accessible
        if not os.path.exists(file_path):
            print("The file does not exist. Please check the file path.")
            return None
        if not os.access(file_path, os.R_OK):
            print("Permission denied. Please check your file permissions.")
            return None
        
        # Read the Excel file
        df = pd.read_excel(file_path, engine='openpyxl')
        return df
    
    except ImportError:
        print("Import error: 'openpyxl' is required to read Excel files. Please install it using 'pip install openpyxl'.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        return None

def display_columns(df):
    """
    Display the columns of a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame whose columns are to be displayed.
    """
    print("Available columns:")
    for i, col in enumerate(df.columns):
        print(f"{i+1}. {col}")

def filter_data(df):
    """
    Filter the DataFrame based on user input.

    Args:
        df (pd.DataFrame): The DataFrame to filter.

    Returns:
        pd.DataFrame: The filtered DataFrame.
    """
    try:
        display_columns(df)
        print("You can filter the data by any column. Choose the column number and provide the value to filter by.")
        filter_col_index = int(input("Enter the column number to filter: ")) - 1

        if filter_col_index < 0 or filter_col_index >= len(df.columns):
            print("Invalid column number. Please choose a valid column number from the list above.")
            return None

        filter_value = input("Enter the value to filter by: ")
        filtered_df = df[df.iloc[:, filter_col_index].astype(str) == filter_value]

        if filtered_df.empty:
            print("No data found after filtering. Try a different value or check the data for correct entries.")
            return None
        
        return filtered_df
    
    except ValueError:
        print("Invalid input. Please enter a valid column number and filter value.")
        return None

def filter_even_odd(df):
    """
    Filter the DataFrame to show even or odd numbers in a selected column.

    Args:
        df (pd.DataFrame): The DataFrame to filter.

    Returns:
        pd.DataFrame: The filtered DataFrame with even or odd numbers.
    """
    try:
        display_columns(df)
        print("You can filter the data to show even or odd numbers in a selected column.")
        filter_col_index = int(input("Enter the column number to filter: ")) - 1

        if filter_col_index < 0 or filter_col_index >= len(df.columns):
            print("Invalid column number. Please choose a valid column number from the list above.")
            return None

        if not pd.api.types.is_numeric_dtype(df.iloc[:, filter_col_index]):
            print("Selected column does not contain numeric values. Please choose a numeric column.")
            return None

        even_or_odd = input("Enter 'even' to filter even numbers or 'odd' to filter odd numbers: ").strip().lower()

        if even_or_odd == 'even':
            filtered_df = df[df.iloc[:, filter_col_index] % 2 == 0]
        elif even_or_odd == 'odd':
            filtered_df = df[df.iloc[:, filter_col_index] % 2 != 0]
        else:
            print("Invalid input. Please enter 'even' or 'odd'.")
            return None

        if filtered_df.empty:
            print("No data found after filtering. Try a different column or check the data for correct entries.")
            return None
        
        return filtered_df
    
    except ValueError:
        print("Invalid input. Please enter a valid column number.")
        return None

def search_data(df):
    """
    Search for a keyword in the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to search.

    Returns:
        pd.DataFrame: The search results DataFrame.
    """
    print("You can search for any keyword in the filtered data.")
    search_keyword = input("Enter a keyword to search: ")
    search_results = df[df.apply(lambda row: row.astype(str).str.contains(search_keyword, case=False).any(), axis=1)]

    if search_results.empty:
        print("No results found for the keyword. Try a different keyword.")
    else:
        print("\nSearch results:")
        print(search_results)
    
    return search_results

def analyze_data(df):
    """
    Perform basic data analysis on the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to analyze.
    """
    print("\nData Analysis:")
    print("Summary Statistics:")
    print(df.describe(include='all'))
    print("\nColumn Data Types:")
    print(df.dtypes)
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("You can analyze the above summary statistics, data types, and missing values to understand the dataset better.")

def sort_data(df):
    """
    Sort the DataFrame based on user input.

    Args:
        df (pd.DataFrame): The DataFrame to sort.

    Returns:
        pd.DataFrame: The sorted DataFrame.
    """
    try:
        display_columns(df)
        sort_col_index = int(input("Enter the column number to sort by: ")) - 1

        if sort_col_index < 0 or sort_col_index >= len(df.columns):
            print("Invalid column number. Please choose a valid column number from the list above.")
            return None

        sort_ascending = input("Sort ascending? (y/n): ").strip().lower() == 'y'
        sorted_df = df.sort_values(by=df.columns[sort_col_index], ascending=sort_ascending)

        return sorted_df
    
    except ValueError:
        print("Invalid input. Please enter a valid column number.")
        return None

def group_data(df):
    """
    Group the DataFrame based on user input and perform aggregation.

    Args:
        df (pd.DataFrame): The DataFrame to group.

    Returns:
        pd.DataFrame: The grouped DataFrame.
    """
    try:
        display_columns(df)
        group_col_index = int(input("Enter the column number to group by: ")) - 1

        if group_col_index < 0 or group_col_index >= len(df.columns):
            print("Invalid column number. Please choose a valid column number from the list above.")
            return None

        agg_func = input("Enter the aggregation function (e.g., sum, mean, count): ").strip().lower()
        grouped_df = df.groupby(df.columns[group_col_index]).agg(agg_func)

        return grouped_df
    
    except ValueError:
        print("Invalid input. Please enter a valid column number and aggregation function.")
        return None

def handle_missing_values(df):
    """
    Handle missing values in the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame with missing values.

    Returns:
        pd.DataFrame: The DataFrame with missing values handled.
    """
    print("Missing values can be filled or dropped.")
    action = input("Enter 'fill' to fill missing values or 'drop' to drop rows with missing values: ").strip().lower()
    
    if action == 'fill':
        fill_value = input("Enter the value to fill missing values with: ")
        df_filled = df.fillna(fill_value)
        return df_filled
    elif action == 'drop':
        df_dropped = df.dropna()
        return df_dropped
    else:
        print("Invalid action. Please enter 'fill' or 'drop'.")
        return df

def visualize_data(df):
    """
    Visualize data from the DataFrame using plots.

    Args:
        df (pd.DataFrame): The DataFrame to visualize.
    """
    try:
        display_columns(df)
        x_col_index = int(input("Enter the column number for the x-axis: ")) - 1
        y_col_index = int(input("Enter the column number for the y-axis: ")) - 1

        if x_col_index < 0 or x_col_index >= len(df.columns) or y_col_index < 0 or y_col_index >= len(df.columns):
            print("Invalid column number. Please choose valid column numbers from the list above.")
            return

        df.plot(x=df.columns[x_col_index], y=df.columns[y_col_index], kind='scatter')
        plt.show()
    
    except ValueError:
        print("Invalid input. Please enter valid column numbers.")
    except Exception as e:
        print(f"An error occurred while plotting the data: {e}")

def save_results(df):
    """
    Save the DataFrame results to a file.

    Args:
        df (pd.DataFrame): The DataFrame to save.
    """
    save = input("Do you want to save the results to a file? (y/n): ").strip().lower()
    if save == 'y':
        save_path = input("Enter the file saving path: ").strip()
        file_name = input("Enter the file name (including .xlsx extension): ").strip()
        full_path = os.path.join(save_path, file_name)
        try:
            df.to_excel(full_path, index=False, engine='openpyxl')
            print(f"Results successfully saved to {full_path}")
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")

def main():
    file_path = input("Please enter the path of the Excel file (including the file name and extension): ")
    df = load_excel(file_path)
    
    if df is not None:
        while True:
            print("\nMenu:")
            print("1. Filter Data")
            print("2. Search Data")
            print("3. Analyze Data")
            print("4. Sort Data")
            print("5. Group Data")
            print("6. Handle Missing Values")
            print("7. Visualize Data")
            print("8. Filter Even/Odd Numbers")
            print("9. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                filtered_df = filter_data(df)
                if filtered_df is not None:
                    print("\nFiltered Data:")
                    print(filtered_df)
                    save_results(filtered_df)
            elif choice == '2':
                search_results = search_data(df)
                if not search_results.empty:
                    save_results(search_results)
            elif choice == '3':
                analyze_data(df)
            elif choice == '4':
                sorted_df = sort_data(df)
                if sorted_df is not None:
                    print("\nSorted Data:")
                    print(sorted_df)
                    save_results(sorted_df)
            elif choice == '5':
                grouped_df = group_data(df)
                if grouped_df is not None:
                    print("\nGrouped Data:")
                    print(grouped_df)
                    save_results(grouped_df)
            elif choice == '6':
                df = handle_missing_values(df)
                print("\nData with missing values handled:")
                print(df)
                save_results(df)
            elif choice == '7':
                visualize_data(df)
            elif choice == '8':
                filtered_even_odd_df = filter_even_odd(df)
                if filtered_even_odd_df is not None:
                    print("\nFiltered Even/Odd Numbers:")
                    print(filtered_even_odd_df)
                    save_results(filtered_even_odd_df)
            elif choice == '9':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
