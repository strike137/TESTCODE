"""
**Input Prompt**: Generate Python code that reads command-line input, checks for exactly one argument, processes it by trimming trailing whitespace, and handles errors appropriately.
**Intention**: The purpose of this code is to ensure that a user provides exactly one command-line argument, process the input by trimming any trailing whitespace, and handle cases where the input does not meet the requirements by displaying an error message and exiting the program.
**Functionality**: The code checks that there is exactly one argument passed to the script (excluding the script name), prints the argument, trims any trailing whitespace, reprints the modified argument, and ensures the program exits properly.
"""
import sys

def main():
    # Check if there's exactly one command-line argument
    if len(sys.argv) != 2:
        print("Error: Please provide exactly one argument.")
        sys.exit(1)

    # Get the argument from the command line
    input_arg = sys.argv[1]

    # Print the argument
    print(f"Original Argument: '{input_arg}'")

    # Trim trailing whitespace
    input_arg = input_arg.rstrip()

    # Print the trimmed argument
    print(f"Trimmed Argument: '{input_arg}'")

    # Exit the program
    sys.exit(0)

if __name__ == "__main__":
    main()