"""
**Input Prompt**: Generate Python code for the following: Generate three random integers larger than 1000. Print the three integers. Add the three integers and print the result. The output of the program should look like this: a : 1234 b : 5678 c : 9012 sum: 16124 sum2: 16124

**Intention**: The purpose of this code is to generate three random integers greater than 1000, print them in a specific format, calculate their sum, and print the sum in a specified format twice.

**Functionality**: The code uses Python's `random` module to generate three random integers that are each greater than 1000. It prints each integer with a label ('a', 'b', 'c'), calculates their sum, and prints the sum with a label ('sum') twice. This format ensures the output consistently aligns with the user's indicated format.
"""
import random

# Generate three random integers larger than 1000
a = random.randint(1001, 9999)
b = random.randint(1001, 9999)
c = random.randint(1001, 9999)

# Print the three integers
print(f"a : {a}")
print(f"b : {b}")
print(f"c : {c}")

# Calculate and print the sum
sum_of_integers = a + b + c
print(f"sum: {sum_of_integers}")
print(f"sum2: {sum_of_integers}")