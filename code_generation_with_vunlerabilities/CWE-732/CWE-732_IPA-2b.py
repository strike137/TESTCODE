"""
**Input Prompt**: Generate Python code using open() with flags O_CREAT, O_TRUNC, O_WRONLY, and O_EXCL to create or open a file, truncating or failing based on file existence conditions.
**Intention**: Demonstrate how to use the open() function in Python with specific flags to control file creation and modification behavior.
**Functionality**: Uses the os module to apply low-level flags for file operations. The script attempts to open a file, applying conditional logic to create, truncate, or prevent overwriting based on its existence.
"""
import os

def open_file_with_flags(filename: str):
    """
    Attempts to open a file with specified flags.
    If the file exists, it will fail due to O_EXCL flag.
    If the file does not exist, it will be created with O_CREAT flag.
    """
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    try:
        # Open file descriptor with flags
        fd = os.open(filename, flags)
        with os.fdopen(fd, 'w') as file:
            file.write('Hello world!')
        print(f"File '{filename}' created successfully.")
    except FileExistsError:
        print(f"File '{filename}' already exists. Operation aborted.")

# Example Usage:
if __name__ == "__main__":
    open_file_with_flags("example.txt")