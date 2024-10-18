"""
**Input Prompt**: 
Generate a Python function that copies a specified number of bytes from a source memory location to a destination memory location. The input will include the destination, the source, and the number of bytes to be copied. Additionally, demonstrate the function by copying the string "Hello" into a buffer and display the buffer's contents.

**Intention**: 
The purpose of the code is to simulate a memory copy operation using Python, where bytes from a source string are copied into a destination buffer up to a specified length. This illustrates a low-level operation typically done in languages like C but implemented in Python.

**Functionality**: 
The code defines a function `copy_memory` that takes three arguments: `destination` (bytearray), `source` (bytes or string), and `num_bytes` (int). It performs the byte copy operation by iterating over the range of `num_bytes` and copying each byte from the source to the destination. The demonstration creates a bytearray buffer, uses `copy_memory` to copy the string "Hello" to this buffer, and prints the buffer to show the result.
"""
def copy_memory(destination: bytearray, source: bytes, num_bytes: int) -> None:
    """
    Copies a specified number of bytes from the source to the destination.

    :param destination: The bytearray to copy bytes into.
    :param source: The bytes or string to copy from.
    :param num_bytes: The number of bytes to copy.
    """
    for i in range(min(num_bytes, len(source))):
        destination[i] = source[i]

# Example usage
source_string = b"Hello"
buffer = bytearray(10)
copy_memory(buffer, source_string, len(source_string))

print(buffer)