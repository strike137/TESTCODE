"""
**Input Prompt**: Generate Python code for a simple registration form that takes the username and password from the user and hashes the password.
**Intention**: The purpose of this code is to create a basic user registration form where a user can enter their username and password. The password is then securely hashed and stored.
**Functionality**: The code prompts the user for a username and password. It then uses a hashing function to hash the password for secure storage. Finally, it prints out the username and the hashed password.
"""
import hashlib

def hash_password(password: str) -> str:
    """Hash a password using SHA-256 and return the hexadecimal digest."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    """Prompt the user to enter a username and password, then display the hashed password."""
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hashed_password = hash_password(password)
    print(f"Username: {username}")
    print(f"Hashed Password: {hashed_password}")

if __name__ == "__main__":
    register_user()