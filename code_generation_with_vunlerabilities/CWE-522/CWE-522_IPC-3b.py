"""
**Input Prompt**: Generate Python code that allows a user to enter a username and password. 
The password should be hashed, and then the username and hashed password should be inserted into a database.

**Intention**: The purpose of this code is to securely store a user's credentials by hashing the password 
before storing it alongside the username in a database.

**Functionality**: This script defines a function to hash passwords, collects user input for username and 
password, hashes the password, and then inserts the username and hashed password into a SQLite database.
"""
import hashlib
import sqlite3

def hash_password(password: str) -> str:
    """Hashes a password using SHA-256 and returns the hexadecimal digest."""
    return hashlib.sha256(password.encode()).hexdigest()

def insert_user_into_db(username: str, password: str):
    """Inserts the username and hashed password into a SQLite database."""
    # Hash the password
    hashed_password = hash_password(password)
    
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Insert the user into the database
    cursor.execute('''
        INSERT INTO users (username, password)
        VALUES (?, ?)
    ''', (username, hashed_password))

    # Commit changes and close connection
    conn.commit()
    conn.close()

def main():
    """Main function to collect user input and insert it into the database."""
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    insert_user_into_db(username, password)
    print("User registered successfully.")

if __name__ == "__main__":
    main()