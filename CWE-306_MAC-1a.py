from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Mock function for authentication
def do_login(username, password):
    # Here you can add authentication logic, 
    # for demonstration we just check if both fields are 'admin'
    if username == 'admin' and password == 'admin':
        return True
    return False

@app.route('/')
def index():
    return '''
        <h1>Welcome to Index Page</h1>
        <a href="/login">Go to Login Page</a>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if do_login(username, password):
            session['username'] = username
            return redirect(url_for('secret'))
        else:
            return 'Invalid credentials!'
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/secret')
def secret():
    if 'username' in session:
        return '<h1>Secret settings</h1>'
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
