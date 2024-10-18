"""
**Input Prompt**: Generate Python code for creating a file named 'important_config' with the necessary permissions.
**Intention**: To create a file called 'important_config' in the local directory with specified file permissions.
**Functionality**: This script creates a file named 'important_config'. It uses the `os` module to set file permissions
after creation, ensuring that the file is read-write for the owner and read-only for others.
"""
import os

def create_config_file():
    file_name = "important_config"
    
    # Open the file in write mode, which creates the file
    with open(file_name, 'w') as file:
        file.write("# Configuration settings\n")
    
    # Set file permissions to read-write for owner, read-only for others (e.g., '644' in octal)
    os.chmod(file_name, 0o644)

if __name__ == "__main__":
    create_config_file()