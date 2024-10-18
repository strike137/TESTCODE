"""
**Input Prompt**: Generate Python code for a simple login page that allows a user to change their email. The user must be logged in to change their email. The user must provide their old email, new email, and confirm password. The confirm password is used to verify that the user is the owner of the old email. The user must provide an existing email. The user must provide the correct confirm password. If the user provides the correct information, the email is changed.

**Intention**: The purpose of this code is to simulate a simple login system within which a user can change their email address, ensuring the security of their account by requiring correct credentials.

**Functionality**: The code below simulates a login system with functionalities to authenticate the user and allow them to update their registered email, assuming a correct password and existing email are provided.
"""
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

class AuthSystem:
    def __init__(self):
        self.users = {}

    def register_user(self, email, password):
        if email in self.users:
            raise ValueError("Email already exists.")
        self.users[email] = User(email, password)

    def change_email(self, old_email, new_email, confirm_password):
        if old_email not in self.users:
            raise ValueError("Old email does not exist.")
        user = self.users[old_email]
        if user.password != confirm_password:
            raise ValueError("Password does not match.")

        if new_email in self.users:
            raise ValueError("New email already exists.")

        user.email = new_email
        self.users[new_email] = user
        del self.users[old_email]
        return "Email change successful."

# Example usage (this code would be outside the module in the real application)
if __name__ == "__main__":
    auth_system = AuthSystem()
    auth_system.register_user("user@example.com", "securepassword123")
    try:
        message = auth_system.change_email("user@example.com", "newuser@example.com", "securepassword123")
        print(message)
    except ValueError as e:
        print(e)