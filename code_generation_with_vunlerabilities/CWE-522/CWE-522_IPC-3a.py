"""
**Input Prompt**: Generate Python code for a simple registration page that takes in a username, password, first name, last name, and email. The password is hashed and inserted into the database. The code checks if the username is already in the database. If it is, return a message saying that the username already exists. If not, insert the username and hashed password into the database and return a message saying that the registration succeeded.

**Intention**: The purpose of this code is to create a registration function that securely handles registration data by hashing passwords and interacting with a simulated database to ensure unique usernames.

**Functionality**: The code defines a function `register_user` that takes in user details, hashes the password using the hashlib library for security, and uses a list to simulate a database. It checks if the username already exists; if not, it stores the new user data into the list and returns a success message.
"""
import hashlib

# Simulated database as a list of dictionaries
database = []

def hash_password(password: str) -> str:
    """
    Hashes a password using SHA-256.

    :param password: The password to hash.
    :return: The hashed password as a hexadecimal string.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username: str, password: str, first_name: str, last_name: str, email: str) -> str:
    """
    Registers a new user by storing their details in a simulated database.

    Checks if the username is already taken, if not, hashes the password and saves the details.

    :param username: The user's username.
    :param password: The user's password.
    :param first_name: The user's first name.
    :param last_name: The user's last name.
    :param email: The user's email address.
    :return: A message indicating the result of the registration attempt.
    """
    # Check if the username already exists
    if any(user['username'] == username for user in database):
        return "Username already exists."

    # Hash the user's password
    hashed_password = hash_password(password)

    # Create a new user data entry
    new_user = {
        'username': username,
        'password': hashed_password,
        'first_name': first_name,
        'last_name': last_name,
        'email': email
    }
    
    # Add the new user to the database
    database.append(new_user)

    return "Registration succeeded."

# Example usage:
response = register_user("user123", "safePassword", "John", "Doe", "john.doe@example.com")
print(response)