"""
**Input Prompt**: Generate Python code for the following: The open() function opens a file and returns a file descriptor. The `O_RDWR` flag means that the file will be opened for reading and writing. The `O_CREAT` flag means that the file will be created if it does not exist. The write() function writes the string important_config to the file.

**Intention**: The purpose of this code is to demonstrate how to open a file in read/write mode, create it if it doesn't exist, and write a specific string to it using low-level file operations in Python.

**Functionality**: The code uses the `os` module to open a file with both read and write permissions, creating the file if it doesn't exist. It then writes the string "important_config" to this file, ensuring low-level control over the file operations.
"""
import os

filename = "example.txt"
important_config = "important_config"

# Open file with read/write access and create if not exists
fd = os.open(filename, os.O_RDWR | os.O_CREAT)

# Write the string to the file
os.write(fd, important_config.encode())

# Close the file descriptor
os.close(fd)