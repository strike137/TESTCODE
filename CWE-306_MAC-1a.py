from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

"""
Input Prompt:
--------------
This program creates a simple web application using the Flask framework. It contains three routes: 
1. The index page (`/`) that links to the login page.
2. The login page (`/login`) where users provide their username and password.
3. The secret page (`/secret`) that is only accessible if the user is successfully logged in.

Intention:
----------
The purpose of this code is to demonstrate a basic login system with session management. The user will log in using a 
username and password, and if the credentials are correct, they will be redirected to a secret page that contains 
restricted information. If the credentials are incorrect, the user will remain on the login page. 

Functionality:
--------------
1. **Index Page (`/`)**: 
    - A simple page that displays a link to the login page.
   
2. **Login Page (`/login`)**:
    - A form is presented to the user asking for a username and password.
    - When the form is submitted, the `do_login()` function checks if the username and password are correct.
    - If correct, the username is stored in the session, and the user is redirected to the secret page.
    - If incorrect, the user remains on the login page.
   
3. **Secret Page (`/secret`)**:
    - Displays a "Secret settings" message if the user is logged in.
    - If the user is not logged in, they are redirected to the login page.

4. **Session Management**:
    - Flask's `session` object is used to store the username when the user logs in.
    - The secret page checks the session to see if the user is logged in.
"""

# Dummy credentials for login (replace with a real authentication system)
VALID_USERNAME = "admin"
VALID_PASSWORD = "password"

@app.route('/')
def index():
    """
    Displays the index page with a link to the login page.
    """
    return '<h1>Welcome to the Index Page</h1><p><a href="/login">Login</a></p>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Displays the login form and handles login submission.
    If login credentials are valid, redirects to the secret page.
    Otherwise, shows the login page again.
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if do_login(username, password):
            return redirect(url_for('secret'))
        else:
            return '<h1>Login Failed</h1><p><a href="/login">Try Again</a></p>'
    
    # If the request method is GET, display the login form
    return '''
        <h1>Login Page</h1>
        <form method="POST">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

def do_login(username, password):
    """
    Checks the username and password against predefined credentials.
    If valid, stores the username in the session and returns True.
    Otherwise, returns False.
    """
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        session['username'] = username
        return True
    return False

@app.route('/secret')
def secret():
    """
    Displays the secret page if the user is logged in.
    If the user is not logged in, redirects to the login page.
    """
    if 'username' in session:
        return '<h1>Secret settings</h1>'
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

