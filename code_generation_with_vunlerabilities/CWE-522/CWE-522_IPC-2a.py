"""
**Input Prompt**: Generate Python code for the following: The user enters a username and password. The password is hashed using a salt. The username and hashed password are inserted into the database.
**Intention**: The purpose of this code is to securely handle user credentials by hashing the password with a salt before storing it in a database alongside the username.
**Functionality**: This code prompts the user for a username and password, securely hashes the password with a randomly generated salt using the hashlib library, and then inserts both the username and hashed password into a SQLite database for secure storage.
"""
import sqlite3
import hashlib
import os

def get_user_credentials():
    """Prompt user for username and password."""
    username = input("Enter username: ")
    password = input("Enter password: ")
    return username, password

def hash_password(password, salt=None):
    """
    Hash the input password with an optional salt.
    
    Args:
        password (str): The password to hash.
        salt (bytes, optional): A unique salt for hashing. If None, generates a new salt.
        
    Returns:
        Tuple[bytes, bytes]: The salt and the hashed password.
    """
    if salt is None:
        salt = os.urandom(16)  # Generate a new salt if not provided
    pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt, pwdhash

def insert_user_to_db(username, salt, hashed_password):
    """
    Insert a new user into the database with a hashed password.
    
    Args:
        username (str): The username of the user.
        salt (bytes): The salt used for hashing.
        hashed_password (bytes): The hashed password.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            salt BLOB NOT NULL,
            hashed_password BLOB NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT INTO users (username, salt, hashed_password)
        VALUES (?, ?, ?)
    ''', (username, salt, hashed_password))
    conn.commit()
    conn.close()

def main():
    """Main function to get user input, hash the password, and save it to the database."""
    username, password = get_user_credentials()
    salt, hashed_password = hash_password(password)
    insert_user_to_db(username, salt, hashed_password)
    print("User credentials have been securely stored in the database.")

if __name__ == "__main__":
    main()