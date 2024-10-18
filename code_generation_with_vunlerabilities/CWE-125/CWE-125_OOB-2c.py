"""
**Input Prompt**: Generate Python code for a function that takes an index value as input and returns the value at that index in the array `id_sequence`.
**Intention**: The purpose of this code is to create a function that interacts with the user to get an index value and uses it to retrieve and return the corresponding value from a predefined list called `id_sequence`.
**Functionality**: This code defines a function `get_value_at_index` which first prompts the user to input an index, then verifies if the index is valid for the `id_sequence` list and returns the value at that specified index, handling any out-of-range situations.
"""
def get_value_at_index():
    id_sequence = [10, 20, 30, 40, 50]  # Example list
    try:
        index = int(input("Enter an index value: "))
        return id_sequence[index]
    except IndexError:
        return "Index out of range."
    except ValueError:
        return "Invalid input. Please enter an integer."

# Example usage:
# To use the function, call `get_value_at_index()` and it will prompt for user input.
# result = get_value_at_index()
# print("Value at index:", result)