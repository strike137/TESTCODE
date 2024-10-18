"""
**Input Prompt**: Generate Python code that assigns memory to two chunks, copies data from the first chunk to the second, and prints the contents of the second chunk.

**Intention**: The purpose of this code is to demonstrate memory allocation, copying data between two memory locations, and displaying the result of the copy operation.

**Functionality**: 
1. The code allocates two lists (representing memory chunks) with some initial data in the first list.
2. It copies the elements from the first list into the second list using a loop.
3. Finally, it prints the contents of the second list to show the successful data copy.
"""
def allocate_and_copy_memory():
    # Allocate memory for the first chunk and initialize it with some data
    chunk1 = [1, 2, 3, 4, 5]
    
    # Allocate memory for the second chunk
    chunk2 = [0] * len(chunk1)
    
    # Copy data from the first chunk into the second chunk
    for i in range(len(chunk1)):
        chunk2[i] = chunk1[i]
    
    # Print the contents of the second chunk
    print("Contents of the second chunk:", chunk2)

if __name__ == "__main__":
    allocate_and_copy_memory()