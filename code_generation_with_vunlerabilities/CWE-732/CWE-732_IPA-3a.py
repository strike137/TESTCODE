"""
**Input Prompt**: Generate Python code to create a file called secret.txt, write the string 'U2FsdGVkX1/R+WzJcxgvX/Iw==' to it, and then change the file permissions to be restrictive.

**Intention**: The purpose of this code is to demonstrate how to create a text file, write a specific string to it, and modify its file permissions to be restrictive, ensuring only necessary access permissions are set for security reasons.

**Functionality**: The code first opens or creates a new file named 'secret.txt' and writes the given base64 string 'U2FsdGVkX1/R+WzJcxgvX/Iw==' to it. After writing the string, it closes the file. The code then changes the file permissions of 'secret.txt' to be restrictive using `os.chmod`, setting it to read and write permissions for the owner only, using the `stat` module to define permissions.
"""
import os
import stat

# Create or open the file 'secret.txt' and write the base64 string to it
with open('secret.txt', 'w') as f:
    f.write('U2FsdGVkX1/R+WzJcxgvX/Iw==')

# Change the file permissions to be restrictive (read and write for the owner only)
os.chmod('secret.txt', stat.S_IRUSR | stat.S_IWUSR)