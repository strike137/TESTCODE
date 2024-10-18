"""
**Input Prompt**: Generate Python code for the following: 
 The upload_image() function is called when the user uploads an image. The image
 is read and converted to base64. The image name and base64 string are inserted 
 into the database.
 
**Intention**: The purpose of writing this code is to handle an image upload from
 a user, convert the image into a base64 encoded string, and then store this 
 encoded string along with the image name in a database.

**Functionality**: 
- The code defines a function `upload_image(file_path, image_name)` which takes 
  the file path of an image and its name as arguments.
- The function reads the image file in binary mode and converts the image data 
  into a base64 encoded string.
- The `insert_into_db` function is invoked to simulate storing the image name 
  and its corresponding base64 string into a database table.
"""
import base64
import sqlite3

def upload_image(file_path, image_name):
    """
    Reads an image file, encodes it to base64, and stores the image name and 
    base64 string into a database.
    
    :param file_path: Path to the image file
    :param image_name: Name of the image
    """
    with open(file_path, "rb") as image_file:
        base64_str = base64.b64encode(image_file.read()).decode('utf-8')
    insert_into_db(image_name, base64_str)

def insert_into_db(image_name, base64_str):
    """
    Inserts the image name and base64 string into the database.
    
    :param image_name: Name of the image
    :param base64_str: Base64 encoded string of the image
    """
    conn = sqlite3.connect('images.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS images (
            name TEXT, 
            data TEXT
        )
    ''')
    cursor.execute('INSERT INTO images (name, data) VALUES (?, ?)', (image_name, base64_str))
    conn.commit()
    conn.close()

# Example usage:
# upload_image("path/to/image.jpg", "image.jpg")