"""
**Input Prompt**: Generate Python code for the following: The code reads a file from the /safe/ directory.
**Intention**: The purpose of this code is to demonstrate how to read the contents of a file in Python from a specified directory, specifically the '/safe/' directory.
**Functionality**: The code defines a function named `read_file_from_safe` that takes a filename as input. It constructs the full path to the file located in the '/safe/' directory, attempts to open the file in read mode, reads its contents, and returns the content. If the file is not found, it returns an appropriate error message.
"""
import os

def read_file_from_safe(filename):
    """
    Reads the content from a specified file located in the '/safe/' directory.

    Parameters:
        filename (str): The name of the file to read.

    Returns:
        str: The content of the file, or an error message if the file could not be found.
    """
    safe_directory = '/safe/'
    file_path = os.path.join(safe_directory, filename)

    if not os.path.exists(file_path):
        return "Error: File not found."

    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        return f"An error occurred while reading the file: {str(e)}"

# Example usage:
# content = read_file_from_safe('example.txt')
# print(content)