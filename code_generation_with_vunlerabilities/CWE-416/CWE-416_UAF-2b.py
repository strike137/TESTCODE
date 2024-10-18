"""
**Input Prompt**: Generate Python code for the following: 
The code reads the contents of a file into a buffer. It then calculates the checksum of the buffer. If the checksum is 0, then the buffer is empty. The number of bytes read and the checksum are saved to another file.

**Intention**: 
The purpose of this code is to read the contents of a specified file, compute the checksum of these contents to determine if the file is empty, and log the results (number of bytes read and computed checksum) into another output file.

**Functionality**: 
The code defines two functions: `calculate_checksum` and `process_file`. The `calculate_checksum` function takes a data buffer as input and returns the checksum by summing up the bytes. The `process_file` function reads the contents of a specified input file into a buffer, calculates its checksum using `calculate_checksum`, and writes the number of bytes read and the checksum into a specified output file.
"""
def calculate_checksum(data):
    """Calculate and return the checksum of a given data buffer."""
    return sum(data)

def process_file(input_file_path, output_file_path):
    """Read the input file, calculate checksum, and write results to the output file."""
    try:
        with open(input_file_path, 'rb') as input_file:
            buffer = input_file.read()
            checksum = calculate_checksum(buffer)
            num_bytes = len(buffer)
        
        with open(output_file_path, 'w') as output_file:
            output_file.write(f"Number of bytes read: {num_bytes}\n")
            output_file.write(f"Checksum: {checksum}\n")
    except (IOError, FileNotFoundError) as e:
        print(f"An error occurred: {e}")

# Example Usage
# process_file('input.txt', 'output.txt')