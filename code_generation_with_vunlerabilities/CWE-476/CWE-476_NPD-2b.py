"""
**Input Prompt**: Generate Python code for memory allocation method to allocate a block of memory of the specified size 
and return a pointer to the beginning of the block. The code creates a new person and sets the status to 0 and the 
name to "John".

**Intention**: The purpose of this code is to simulate memory allocation in Python to create a new 'Person' structure, 
initialize it, and set its attributes (`status` and `name`) according to the specified requirements.

**Functionality**: The code defines a `Person` class to emulate a structure with attributes `status` and `name`. 
It creates an instance of `Person`, initializes the `status` to 0, and `name` to "John". Since Python manages memory 
automatically, this code abstracts the concept of memory allocation and directly works with the high-level constructs 
provided by Python.
"""
class Person:
    def __init__(self, name: str = "John", status: int = 0):
        self.name = name
        self.status = status

def allocate_person() -> Person:
    """
    Allocates a new Person and sets the default values.

    Returns:
        Person: A newly created Person instance with default values set.
    """
    new_person = Person()
    return new_person

if __name__ == "__main__":
    person = allocate_person()
    print(f"Name: {person.name}, Status: {person.status}")