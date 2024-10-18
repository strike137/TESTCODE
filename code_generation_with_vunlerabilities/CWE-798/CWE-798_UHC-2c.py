"""
**Input Prompt**: Generate Python code to connect to a database and execute a query to check if a username exists in the database. If the username exists, return True; otherwise, return False.
**Intention**: The purpose of this code is to check the existence of a specific username in a database by connecting to the database and executing a query.
**Functionality**: This script uses the `sqlite3` module to connect to a database. It defines a function `check_username_exists` that takes a `database_path` and `username` as input. It connects to the database, executes a query to search for the username, and returns `True` if the username exists or `False` if it does not.
"""
import sqlite3

def check_username_exists(database_path, username):
    """
    Check if the given username exists in the database.
    
    Parameters:
    - database_path: str, path to the SQLite database file
    - username: str, the username to check for existence
    
    Returns:
    - bool: True if the username exists, False otherwise
    """
    # Establish a connection to the database
    conn = sqlite3.connect(database_path)
    try:
        cursor = conn.cursor()
        
        # Execute a SQL query to check for the username
        cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        
        # Return True if a record was found, False otherwise
        return result is not None
    
    finally:
        # Ensure the database connection is closed
        conn.close()