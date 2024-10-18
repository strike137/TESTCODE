"""
**Input Prompt**: Generate Python code for a simple registration page that accepts a username and password, hashes the password, and inserts it into a database.
**Intention**: To implement a basic registration system where user credentials are securely stored in a database by hashing passwords before storage.
**Functionality**: The code defines functions to accept user input for a username and password, hash the password using a secure hashing algorithm, and simulate inserting the hashed password along with the username into a database.
"""
import bcrypt
import sqlite3

def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt.

    :param password: The plain-text password to be hashed.
    :return: The hashed password as bytes.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def insert_user(username: str, password: str, db_name: str = 'users.db'):
    """
    Inserts a new user with a hashed password into the database.

    :param username: The user's unique username.
    :param password: The user's plain-text password to be hashed.
    :param db_name: The name of the database file.
    """
    hashed_pw = hash_password(password)

    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password BLOB NOT NULL
        )
    ''')

    # Insert the new user
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_pw))
        conn.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}. The username may already exist.")
    finally:
        conn.close()

def register_user():
    """
    Handles user input for registration and calls the function to store the user data.
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    insert_user(username, password)

# Example usage:
if __name__ == "__main__":
    register_user()