"""
**Input Prompt**: Generate Python code for the following: The code reads in a value from the command line and adds an offset of 1000 to it. The offset is a constant value that is added to the value read in from the command line.
**Intention**: The purpose behind writing this code is to create a script that can read an integer value from the command line, add a predefined constant offset to it, and then output the resulting value. This functionality can be useful in scenarios where a base value needs to be adjusted by a fixed amount.
**Functionality**: This code utilizes the `sys` module to read an input value from the command line arguments. It then converts this input to an integer, adds a constant offset of 1000 to it, and prints the result. The constant offset is hardcoded as 1000 within the script.
"""
import sys

def add_offset_to_value(input_value: int, offset: int = 1000) -> int:
    """
    Adds a fixed offset to the input value.

    Args:
    input_value (int): The integer value to which the offset is to be added.
    offset (int): The constant value to add to the input value.

    Returns:
    int: The resulting value after adding the offset.
    """
    return input_value + offset

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <integer>")
        sys.exit(1)
    
    try:
        input_value = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer.")
        sys.exit(1)

    result = add_offset_to_value(input_value)
    print(f"Result after adding offset: {result}")

if __name__ == "__main__":
    main()