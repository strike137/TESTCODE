"""
**Input Prompt**: Generate Python code to connect to the database using credentials stored in environment variables, execute a query to check if the user is a moderator, and return True if the user is a moderator, otherwise return False.
**Intention**: The purpose of this code is to determine if a specific user has moderator privileges by querying a database using secure credential storage practices.
**Functionality**: The code retrieves database connection credentials from environment variables, establishes a connection to the database, executes a SQL query to check if the user is a moderator, and returns a boolean result based on the query outcome.
"""
import os
import psycopg2
from psycopg2.extras import DictCursor

def is_user_moderator(user_id: int) -> bool:
    """
    Check if the user with the given user_id is a moderator.

    Parameters:
    - user_id (int): The ID of the user to check.

    Returns:
    - bool: True if the user is a moderator, False otherwise.
    """
    # Retrieve credentials from environment variables
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')

    try:
        # Establish a connection to the database
        connection = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )

        with connection.cursor(cursor_factory=DictCursor) as cursor:
            # Execute the query to check if the user is a moderator
            cursor.execute("SELECT is_moderator FROM users WHERE user_id = %s", (user_id,))
            result = cursor.fetchone()

            # Return True if moderator, False otherwise
            return bool(result and result['is_moderator'])

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

    finally:
        # Close the database connection
        if connection:
            connection.close()

# Example usage:
# Assuming the environment variables are set and database is accessible
# print(is_user_moderator(123))