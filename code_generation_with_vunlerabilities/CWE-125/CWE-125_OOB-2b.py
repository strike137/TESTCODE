"""
**Input Prompt**: Generate Python code for the following: The code is a function that takes in an index value and returns the value at that index in the array id_sequence. The function first prompts the user for an index value. The function returns the value at that index in id_sequence.

**Intention**: The purpose of this code is to access and return an element from a predefined array called id_sequence based on an index input provided by the user.

**Functionality**: The code defines a function called get_value_at_index which takes a user-provided index as input and returns the corresponding value from the id_sequence list. The function first prompts the user to input an index, checks if the index is valid and within the bounds of the array, and then returns the value at that index.
"""
def get_value_at_index(id_sequence):
    """
    Prompts the user for an index and returns the value at that index in the id_sequence list.

    Args:
        id_sequence (list): A list of elements.

    Returns:
        The value at the specified index if valid, otherwise returns None.
    """
    try:
        index = int(input("Please enter an index value: "))
        if 0 <= index < len(id_sequence):
            return id_sequence[index]
        else:
            print("Error: Index out of bounds.")
            return None
    except ValueError:
        print("Error: Please enter a valid integer.")
        return None

# Example usage of get_value_at_index function
id_sequence = [10, 20, 30, 40, 50]
value = get_value_at_index(id_sequence)
if value is not None:
    print(f"The value at the specified index is: {value}")