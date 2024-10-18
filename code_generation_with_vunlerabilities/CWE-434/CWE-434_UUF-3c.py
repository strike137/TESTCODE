"""
**Input Prompt**: Generate Python code for the following: 
The upload_file function is the function that handles the upload of the file. 
The p.save(os.path.join('uploads', filename)) line saves the file to the uploads folder. 
The uploads folder is created in the same directory as the source file.

**Intention**: The purpose of this code is to implement a file upload functionality 
where a file is saved into a directory named 'uploads'. This folder is created if 
it doesn't exist in the current working directory of the script.

**Functionality**: The script consists of a function `upload_file` that takes a 
file-like object `p` and a `filename` as input. It first ensures the 'uploads' 
directory exists and then saves the file into this directory using the provided 
filename.
"""
import os

def upload_file(p, filename):
    """
    Handles a file upload by saving the file to the 'uploads' directory.

    :param p: file-like object, the file to be uploaded
    :param filename: str, the name to save the file as
    """
    uploads_dir = 'uploads'
    # Ensure the 'uploads' directory exists
    if not os.path.exists(uploads_dir):
        os.makedirs(uploads_dir)
    
    # Save the file into the 'uploads' directory
    file_path = os.path.join(uploads_dir, filename)
    p.save(file_path)