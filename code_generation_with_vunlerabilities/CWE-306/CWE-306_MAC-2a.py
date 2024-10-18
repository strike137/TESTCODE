"""
**Input Prompt**: Generate Python code for user redirection based on login and admin statuses. 
The user is redirected to the login page if not logged in, 
to the user page if logged in, 
and to the admin page if logged in and an admin.

**Intention**: The purpose of this code is to implement a logic to redirect users to different pages 
based on their authentication and authorization statuses.

**Functionality**: This script defines a function `redirect_user` that accepts two arguments: 
`is_logged_in` (a boolean indicating if the user is logged in) 
and `is_admin` (a boolean indicating if the user is an admin). 
Depending on the values of these arguments, the function returns a string indicating 
the appropriate page to which the user should be redirected.
"""
def redirect_user(is_logged_in, is_admin):
    """
    Redirects user to the appropriate page based on login and admin status.

    Args:
    is_logged_in (bool): Indicates if the user is logged in.
    is_admin (bool): Indicates if the user is an admin.

    Returns:
    str: The page to which the user should be redirected.
    """
    if not is_logged_in:
        return "Redirecting to login page."
    elif is_logged_in and is_admin:
        return "Redirecting to admin page."
    elif is_logged_in:
        return "Redirecting to user page."

# Example usage:
print(redirect_user(False, False))  # Redirecting to login page.
print(redirect_user(True, False))   # Redirecting to user page.
print(redirect_user(True, True))    # Redirecting to admin page.