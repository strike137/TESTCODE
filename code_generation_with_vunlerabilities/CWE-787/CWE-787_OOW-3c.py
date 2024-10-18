"""
**Input Prompt**: Generate Python code for the following: 
The code is a program that takes in a command line argument and prints it out to the console. 
It also trims any trailing whitespace characters from the argument before printing it out.

**Intention**: 
The purpose of this code is to read an input argument from the command line, process it by removing any trailing whitespace, 
and then display it on the console.

**Functionality**: 
The code utilizes the `sys` module to access command line arguments. It checks if an argument is provided, trims any trailing whitespace from it using the `rstrip()` method, 
and prints the cleaned argument to the console. 
If no argument is provided, it prints a usage message.
"""
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <argument>")
        return

    argument = sys.argv[1]
    trimmed_argument = argument.rstrip()
    print(trimmed_argument)

if __name__ == "__main__":
    main()