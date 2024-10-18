"""
**Input Prompt**: Generate Python code that takes an index as an argument and prints the corresponding argument from the command line arguments. For example, if the program is called with './argv_index 1', it will print the second argument, which is the first argument the user typed after the program name.

**Intention**: The purpose of this code is to retrieve and print a specific command line argument based on the index provided by the user. This allows users to extract and utilize specific parts of the command line input.

**Functionality**: The code uses the `sys` module to access command line arguments. It takes an index as a command line argument, adjusts it to account for Python's zero-based indexing, and prints the corresponding argument. If the specified index is out of range, it prints an error message.
"""
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <index>")
        return

    try:
        index = int(sys.argv[1])
        print(sys.argv[index + 1])
    except ValueError:
        print("Please provide a valid integer index.")
    except IndexError:
        print("Index out of range. Make sure the specified index is within bounds.")

if __name__ == "__main__":
    main()