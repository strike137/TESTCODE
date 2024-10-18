"""
**Input Prompt**: Generate Python code for the following: The upload_image() function is called when the user uploads an image. The image is read and encoded using base64. The encoded image is written to a file.

**Intention**: The purpose of this code is to define a function that processes an uploaded image by reading it, encoding it using Base64, and then saving the encoded data to a file.

**Functionality**: The code defines the `upload_image` function which accepts an image file path as input, reads the image binary data, encodes it using Base64 encoding, and writes the encoded string to a specified output file.
"""
import base64

def upload_image(image_path: str, output_file: str) -> None:
    """
    Reads an image file, encodes it using Base64, and writes the encoded data to a file.

    :param image_path: The path of the image file to be encoded.
    :param output_file: The file path where the encoded image will be saved.
    """
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
    
    encoded_image = base64.b64encode(image_data).decode('utf-8')
    
    with open(output_file, "w") as file:
        file.write(encoded_image)