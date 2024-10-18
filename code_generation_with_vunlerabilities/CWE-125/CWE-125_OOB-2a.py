"""
**Input Prompt**: Generate Python code for a function that accepts an index value 
and returns the value at that index from the array `id_sequence`. The main function 
should prompt the user for an index value and use the function to obtain and print
the value from the array `id_sequence`.

**Intention**: The purpose of this code is to create a Python script that allows users to 
interactively retrieve values from a predefined list using an index value. This demonstrates 
basic list indexing and handling of user input in Python.

**Functionality**: The script consists of two parts:
1. A function `get_value_from_index` that takes an index and retrieves the corresponding 
value from the list `id_sequence`. It checks for valid indices and returns `None` if the 
index is out of range.
2. A main function that prompts the user for an index, calls `get_value_from_index`
with this index, and prints the result. The main function handles invalid input 
by notifying the user if the index is not a valid integer.
"""
id_sequence = [101, 202, 303, 404, 505]

def get_value_from_index(index):
    """
    Returns the value at the provided index from the id_sequence list.
    
    Parameters:
    index (int): The index of the desired value in the id_sequence list.
    
    Returns:
    int or None: The value at the provided index if valid, otherwise None.
    """
    if 0 <= index < len(id_sequence):
        return id_sequence[index]
    else:
        return None

def main():
    """Prompts user for an index and prints the value from id_sequence at that index."""
    try:
        user_input = int(input("Enter an index value to retrieve from id_sequence: "))
        value = get_value_from_index(user_input)
        if value is not None:
            print(f"Value at index {user_input}: {value}")
        else:
            print("Index out of range.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()