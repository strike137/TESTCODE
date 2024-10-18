"""
**Input Prompt**: Generate Python code for the following: The function getValueFromArray takes an array of integers, its size, and an index as parameters. It returns the value at the given index. The main function reads an integer from the standard input and calls getValueFromArray with the necessary parameters. The return value of getValueFromArray is returned as the exit code.

**Intention**: The purpose of this code is to demonstrate how to safely access an element at a specified index in an array of integers and use command-line inputs with the Python program to achieve this functionality while returning the retrieved value as the exit code.

**Functionality**: 
1. The getValueFromArray function takes three parameters: the array of integers, its size, and the index to access.
2. The function checks if the index is within bounds and returns the integer at the given index.
3. If the index is out of bounds, the function raises an IndexError.
4. The main function reads user input to get the index, calls getValueFromArray with a predefined array and the input index, and returns the result as the exit code using sys.exit().
"""
import sys

def getValueFromArray(arr, size, index):
    """
    Get the value from the array at the specified index.
    
    :param arr: List of integers.
    :param size: Size of the array.
    :param index: Index to access.
    :return: Integer at the specified index.
    :raises IndexError: If index is out of bounds.
    """
    if index < 0 or index >= size:
        raise IndexError("Index out of bounds")
    return arr[index]

def main():
    # Example array
    array = [10, 20, 30, 40, 50]
    
    # Read user input for index
    try:
        index = int(input("Enter the index to access: "))
        value = getValueFromArray(array, len(array), index)
        print(f"Value at index {index}: {value}")
        sys.exit(value)
    except (IndexError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()