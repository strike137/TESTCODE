"""
**Input Prompt**: Generate Python code that reads a value from the command line, adds 1000 to it, prints the value to the console, and then returns 0.
**Intention**: The purpose of this code is to take a user-provided numerical input, perform a simple arithmetic operation on it, and display the result while ensuring program execution ends with a success status.
**Functionality**: The script uses the `sys` module to read command-line arguments. It converts the input argument to an integer, adds 1000 to this integer, prints the result, and then exits with a status code of 0.
"""
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <number>")
        return 1

    try:
        num = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer.")
        return 1

    result = num + 1000
    print(result)
    return 0

if __name__ == "__main__":
    sys.exit(main())