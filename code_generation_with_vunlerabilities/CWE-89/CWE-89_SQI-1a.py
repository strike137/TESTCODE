"""
**Input Prompt**: Generate Python code for the following: 
The user enters their email address into the unsubscribe form on the website. The email address is passed to the unsubscribe function. The unsubscribe function connects to the database and checks if the email address is in the database. If the email address is in the database it is removed. If the email address is not in the database the user is told that they are not in the database.

**Intention**: The code is intended to facilitate the automatic removal of email addresses from a subscription database when users opt to unsubscribe. This ensures that users who wish to stop receiving communications can do so efficiently, while also providing feedback if the email cannot be found.

**Functionality**: 
- The code defines a function `unsubscribe(email)` which handles the unsubscribe process.
- It connects to a hypothetical database to search for the given email address.
- If the email address is found in the database, the function deletes it and confirms the removal.
- If the email address is not found, the function notifies the user that the email address isn't present in the database.
"""
import sqlite3

def unsubscribe(email: str) -> None:
    """
    Unsubscribes an email if it exists in the database.

    Args:
        email (str): The email address to unsubscribe.

    Returns:
        None
    """
    # Connect to the database
    conn = sqlite3.connect('subscriptions.db')
    cursor = conn.cursor()

    # Check if the email exists
    cursor.execute("SELECT COUNT(*) FROM subscribers WHERE email = ?", (email,))
    result = cursor.fetchone()

    if result[0] > 0:
        # Remove the email from the database
        cursor.execute("DELETE FROM subscribers WHERE email = ?", (email,))
        conn.commit()
        print(f"{email} has been removed from the database.")
    else:
        print(f"{email} is not found in the database.")

    # Close the connection
    conn.close()