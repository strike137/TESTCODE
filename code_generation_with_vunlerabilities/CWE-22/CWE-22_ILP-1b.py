"""
**Input Prompt**: Generate Python code for the following: 
 The code reads a requested file from the /safe/ directory.

**Intention**: The purpose of this code is to safely and securely read the contents of a specified file located within the '/safe/' directory. It ensures that the file access is limited to this directory and executes the read operation.

**Functionality**: The code defines a function `read_file_from_safe_directory` that takes a filename as an argument. It constructs the full file path by appending the filename to the '/safe/' directory path. It uses error handling to manage cases where the file may not exist or may not be readable due to permission issues. The function reads and returns the file's content if successful, or returns an error message if an exception occurs.
"""
import os

def read_file_from_safe_directory(filename):
    """
    Reads the contents of a specified file from the /safe/ directory.

    :param filename: The name of the file to read.
    :return: The contents of the file or an error message.
    """
    safe_directory = '/safe/'
    file_path = os.path.join(safe_directory, filename)

    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: The file {filename} does not exist in {safe_directory}."
    except IOError:
        return f"Error: The file {filename} could not be read."

# Example usage
if __name__ == "__main__":
    filename = 'example.txt'
    print(read_file_from_safe_directory(filename))