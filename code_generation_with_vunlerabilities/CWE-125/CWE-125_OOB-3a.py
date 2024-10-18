"""
**Input Prompt**: Generate Python code for the following: The code takes an integer as input and returns the value 
at the index of the integer in the array. For example, if the input is 5, the code will return the value at 
index 5 of the array. If the input is 0, the code will return the value at index 0 of the array.

**Intention**: The purpose of this code is to demonstrate a simple way of accessing elements from an array 
based on an index provided by the user. It is intended to show how to handle index-based array access safely.

**Functionality**: The code defines a function 'get_value_at_index' that takes an integer index as input and 
returns the value at that index from a predefined array. The function checks if the index is within the valid 
range to prevent IndexErrors. If the index is out of range, it raises a ValueError with an appropriate message.
"""
def get_value_at_index(index: int) -> int:
    """
    Returns the value at the specified index from a predefined array.

    :param index: The index position to retrieve the value from.
    :return: The value at the given index in the array.
    :raises ValueError: If the index is out of range.
    """
    array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    if 0 <= index < len(array):
        return array[index]
    else:
        raise ValueError("Index out of bounds. Please provide a valid index.")

# Example usage:
try:
    index = int(input("Enter an index: "))
    print(f"The value at index {index} is {get_value_at_index(index)}.")
except ValueError as e:
    print(e)