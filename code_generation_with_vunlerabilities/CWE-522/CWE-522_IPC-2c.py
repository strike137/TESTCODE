"""
**Input Prompt**: 
Generate Python code for the following:
The code is a simple registration form that takes in a username and password. 
The password is then hashed using an algorithm. The salt is generated using a function. 
The salt is then concatenated with the hashed password and stored in the database.

**Intention**: 
The purpose of this code is to create a simplistic registration simulation where user credentials 
are accepted and securely stored by hashing the password, salting it, and then concatenating 
the salt to ensure added security.

**Functionality**: 
The code defines a basic registration system with three main functionalities:
1. It accepts a username and a password from the user.
2. It generates a secure random salt, hashes the provided password using a cryptographic algorithm 
   (SHA256 in this case), and combines the hash with the salt.
3. It stores the username along with the salted and hashed password in a simulated in-memory database.
"""
import hashlib
import os

class SimpleDatabase:
    def __init__(self):
        """Simulates a database using an in-memory dictionary."""
        self.users = {}

    def store_user(self, username, password_hash):
        """Stores the username and password hash in the database."""
        self.users[username] = password_hash

def hash_password(password, salt_length=16):
    """
    Hashes the password with a generated salt.

    :param password: The password to hash.
    :param salt_length: The length of the salt. Defaults to 16 bytes.
    :return: A tuple containing the generated salt and the salted, hashed password.
    """
    salt = os.urandom(salt_length)
    password_hash = hashlib.sha256(salt + password.encode()).hexdigest()
    return salt, password_hash

def register_user(database, username, password):
    """
    Registers a new user by hashing their password and storing it in the database.

    :param database: An instance of the SimpleDatabase.
    :param username: The username of the user.
    :param password: The password of the user.
    """
    salt, hashed_password = hash_password(password)
    password_storage = salt.hex() + '$' + hashed_password
    database.store_user(username, password_storage)

if __name__ == "__main__":
    db = SimpleDatabase()
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    register_user(db, username, password)
    print("User registered successfully!")
    print("Database contents:", db.users)