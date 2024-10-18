"""
**Input Prompt**: Generate Python code for the following:
    The code is a simple login page that allows a user to change their email. 
    The user must be logged in to change their email. 
    The user must enter their old email, new email, and confirm password. 
    The user must also enter the correct password to change their email. 
    The user must enter a new email that is different from their old email.

**Intention**: 
    The purpose of this code is to implement a basic functionality for a login system 
    where users can change their email address securely by verifying their identity 
    through an existing session, password confirmation, and making sure the new email 
    is indeed different from the old one.

**Functionality**: 
    The code defines a simple command-line interface (CLI) interaction where a user 
    can log in with a username and password. Once logged in, the user has the option 
    to change their email by entering their old email, a new email which must be 
    different from the old one, and confirming their password. Appropriate validation 
    and messages indicate whether the email update was successful or failed.
"""
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.logged_in = False

    def login(self, entered_password):
        if self.password == entered_password:
            self.logged_in = True
            return True
        return False

    def change_email(self, old_email, new_email, entered_password):
        if not self.logged_in:
            return "User must be logged in to change email."
        if self.email != old_email:
            return "Old email does not match current email."
        if new_email == old_email:
            return "New email must be different from old email."
        if self.password != entered_password:
            return "Incorrect password."
        
        self.email = new_email
        return "Email updated successfully."

def main():
    # Predefined user details for demonstration
    user = User("user1", "old_email@example.com", "password123")

    # Simulated user input
    print("Logging in...")
    if user.login("password123"):
        print("Login successful.")
        
        print("Changing email...")
        result = user.change_email("old_email@example.com", "new_email@example.com", "password123")
        print(result)
    else:
        print("Failed to log in.")

if __name__ == "__main__":
    main()