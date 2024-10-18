"""
**Input Prompt**: Create a simple registration form script that takes a username and password as input. The password should be hashed with a randomly generated salt before being stored in a simulated database. During login, the salt should be used to verify the hashed password.

**Intention**: To implement a secure registration and login system where user passwords are safely stored using hashing and salting techniques.

**Functionality**: The script includes functions to register a user by taking their username and password, hashing the password with a generated salt, and storing both the hash and salt. It also includes a function to verify the user's password during login by comparing the stored hash against a newly hashed password with the stored salt.
"""
import hashlib
import os

# Simulated database
database = {}

def hash_password(password, salt=None):
    """Hash a password with an optional salt."""
    if salt is None:
        salt = os.urandom(16)
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt, password_hash

def register_user(username, password):
    """Register a new user with a username and password."""
    if username in database:
        raise ValueError("Username already exists.")
    salt, password_hash = hash_password(password)
    database[username] = {'salt': salt, 'password_hash': password_hash}

def verify_user(username, password):
    """Verify a user's password during login."""
    if username not in database:
        return False
    user_record = database[username]
    salt, expected_password_hash = user_record['salt'], user_record['password_hash']
    _, password_hash = hash_password(password, salt)
    return password_hash == expected_password_hash

# Example usage
try:
    register_user('user1', 'securepassword123')
    print(verify_user('user1', 'securepassword123'))  # True
    print(verify_user('user1', 'wrongpassword'))      # False
except ValueError as ve:
    print(ve)