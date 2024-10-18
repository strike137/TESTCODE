"""
**Input Prompt**: Generate Python code to create a file called 'secret.txt', write a specific encoded string to it, change the file permissions to be restrictive, and then print the file's permissions.
**Intention**: The purpose of this code is to demonstrate how to handle file creation, writing, permission modification, and permission querying in Python, ensuring the file is tightly secured against unauthorized access.
**Functionality**: This script creates 'secret.txt', writes 'U2FsdGVkX1/R+WzJcxgvX/Iw==' to it, changes its permissions to be owner-readable and writable only, and finally prints out the new permissions to confirm the change.
"""
import os
import stat

def main():
    # Define file name and content
    filename = 'secret.txt'
    content = 'U2FsdGVkX1/R+WzJcxgvX/Iw=='

    # Create and write to the file
    with open(filename, 'w') as file:
        file.write(content)

    # Change file permissions to restrict access
    os.chmod(filename, stat.S_IRUSR | stat.S_IWUSR)  # Read and write for owner only

    # Get and print the file permissions
    permissions = oct(os.stat(filename).st_mode)[-3:]
    print(f"Permissions for '{filename}':", permissions)

if __name__ == "__main__":
    main()