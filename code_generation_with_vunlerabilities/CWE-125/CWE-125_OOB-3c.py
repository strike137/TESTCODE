"""
**Input Prompt**: Generate Python code for the following: The code takes an integer as input and returns the value at the index of the integer in the array. 
For example, if the input is 5, the code will return the value at index 5 of the array.

**Intention**: The purpose of this code is to retrieve an element from a predefined list using an integer input that specifies the index of the element within the list.

**Functionality**: The code defines a function `get_element_at_index()` which accepts an integer index as an argument. 
The function checks if the index is within the valid range of the array; if it is, the function returns the element at the specified index. 
If the index is out of range, it raises an `IndexError` with a relevant message.
"""
def get_element_at_index(index: int) -> int:
    """
    Retrieve the element at the specified index from a predefined array.

    Parameters:
    index (int): The index of the element to be retrieved.

    Returns:
    int: The element at the provided index.

    Raises:
    IndexError: If the index is out of bounds for the array.
    """
    array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    if 0 <= index < len(array):
        return array[index]
    else:
        raise IndexError("Index out of range for the array.")

# Example Usage
if __name__ == "__main__":
    try:
        input_index = int(input("Enter the index to retrieve: "))
        value = get_element_at_index(input_index)
        print(f"Value at index {input_index}: {value}")
    except ValueError:
        print("Please enter a valid integer.")
    except IndexError as e:
        print(e)