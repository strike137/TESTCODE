"""
**Input Prompt**: Generate Python code for a function that copies a number of bytes from one memory location to another.
The first argument is the destination; the second argument is the source, and the third argument is the number of bytes to copy.
The code copies the message to the buffer.

**Intention**: The purpose of writing this code is to demonstrate how raw bytes can be copied from one byte-like object to another
using Python, mimicking behavior similar to that of low-level memory operations seen in languages like C.

**Functionality**: The code defines a function named `copy_bytes` that takes three parameters: `destination`, `source`, 
and `num_bytes`. The function performs checks to ensure the inputs are valid (both destination and source are mutable 
byte-like objects) and then copies the specified number of bytes from the source to the destination.
"""
def copy_bytes(destination: bytearray, source: bytes, num_bytes: int) -> None:
    """
    Copies a specified number of bytes from source to destination.

    Args:
        destination (bytearray): The destination where bytes are copied to.
        source (bytes): The source from where bytes are copied.
        num_bytes (int): The number of bytes to copy.

    Raises:
        ValueError: If num_bytes exceeds the length of either the source or the destination.
    """
    if not isinstance(destination, bytearray):
        raise TypeError("Destination must be a bytearray.")
    
    if not isinstance(source, (bytes, bytearray)):
        raise TypeError("Source must be bytes or bytearray.")
    
    if num_bytes > len(source) or num_bytes > len(destination):
        raise ValueError("Number of bytes to copy is out of range.")
    
    for i in range(num_bytes):
        destination[i] = source[i]