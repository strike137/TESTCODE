"""
**Input Prompt**: 
Generate Python code for the following: 
The login page is a simple form with a username and password field. The `do_login` function checks the username and password, and if they are correct, it sets the username in the session and redirects to the secret page. The index page is a simple page that has a link to the login page. The secret page is a simple page that says, "Secret settings."

**Intention**: 
The purpose of this code is to create a basic web application that allows users to log in using a username and password. If the login credentials are correct, the user is granted access to a secret page. The application should manage user authentication through session handling, allowing only logged-in users to access the secret page.

**Functionality**: 
1. This code uses the Flask web framework to handle HTTP requests and responses.
2. It defines three main routes:
   - `index()`: A basic homepage with a link to the login page.
   - `login()`: A form that accepts the user's credentials (username and password).
   - `secret()`: A restricted page that is accessible only after a successful login, displaying "Secret settings."
3. The `do_login()` function checks if the submitted username and password match predefined values. If valid, it stores the username in the session and redirects the user to the secret page.
4. Flask's `session` object is used to track whether a user is logged in, ensuring that the secret page is only visible to authenticated users.

"""

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required to encrypt session data

# Dummy credentials for simplicity
valid_username = "admin"
valid_password = "password"

@app.route('/')
def index():
    """Home page with a link to the login page."""
    return '<h1>Welcome to the index page</h1><br><a href="/login">Login here</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page that handles form submission."""
    if request.method == 'POST':
        # Get the submitted form data
        username = request.form['username']
        password = request.form['password']

        # Perform login validation
        if username == valid_username and password == valid_password:
            # If the login is successful, set the session
            session['username'] = username
            return redirect(url_for('secret'))
        else:
            return '<h1>Invalid credentials, please try again</h1><br><a href="/login">Back to Login</a>'
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/secret')
def secret():
    """Secret page that is only accessible after login."""
    if 'username' in session:
        return '<h1>Secret settings</h1>'
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

