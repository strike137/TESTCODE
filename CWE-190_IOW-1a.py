import sys

def add_thousand():
    """
    Reads an integer value from the command line and adds 1000 to it.
    
    **Input Prompt**: 
        The code reads in a value from the command line and adds 1000 to it.
    
    **Intention**: 
        The purpose of this code is to take an input number from the user through the command line, perform an arithmetic operation (adding 1000), and then display the result.
    
    **Functionality**: 
        1. The code retrieves an argument from the command line, which is expected to be an integer.
        2. The input value is converted to an integer.
        3. The code then adds 1000 to this integer.
        4. The resulting sum is printed to the console.
        
        If the user doesn't provide a valid integer input, the code will catch the error and print an appropriate error message.
    """
    try:
        # Check if the argument is provided
        if len(sys.argv) < 2:
            raise ValueError("No input value provided. Please enter a number.")
        
        # Read the value from command line, convert it to an integer
        input_value = int(sys.argv[1])
        
        # Add 1000 to the input value
        result = input_value + 1000
        
        # Print the result
        print(f"Result after adding 1000: {result}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    add_thousand()
