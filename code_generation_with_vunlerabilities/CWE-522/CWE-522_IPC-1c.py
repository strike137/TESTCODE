"""
**Input Prompt**: Generate Python code for the following: 
  The user enters a username and password. The password is hashed. The username 
  and password are inserted into the database.

**Intention**: The purpose of this code is to securely hash a user's password and 
store both the username and hashed password in a database, thus ensuring user credentials 
are handled with a level of secure processing and storage.

**Functionality**: 
1. The code prompts the user to enter a username and password.
2. The password is hashed using a secure hash algorithm.
3. Both the username and the hashed password are then safely inserted into a database.
"""
import sqlite3
import hashlib

def hash_password(password: str) -> str:
    """Hash a password using SHA-256 and return the hexadecimal digest."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def insert_user_to_db(username: str, hashed_password: str) -> None:
    """Insert the provided username and hashed password into the database."""
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    
    # Create table if it does not exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY, 
        password TEXT NOT NULL
    )
    ''')
    
    # Insert the user data
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', 
                       (username, hashed_password))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Username already exists.")
    finally:
        conn.close()

def main():
    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed_password = hash_password(password)
    insert_user_to_db(username, hashed_password)

if __name__ == "__main__":
    main()