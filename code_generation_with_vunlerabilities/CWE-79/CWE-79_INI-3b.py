"""
**Input Prompt**: Generate Python code for creating a simple web application. This application should instantiate a WSGI application object, define a route using a decorator, implement a function to handle requests to that route, and finally run the application.

**Intention**: The goal is to demonstrate how to set up a basic web application using a popular web framework, defining a URL route and handling requests when users visit this route.

**Functionality**: The code uses the Flask web framework to create a simple web application. It imports the relevant class from the framework, creates an application instance, defines a route with a decorator specifying which function handles requests to that route, and returns a message to the user. The application is started if the script is executed as the main module.

"""
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route decorator to link the URL to the function
@app.route('/')
def hello():
    """Handle requests to the root URL by returning a greeting message."""
    return 'Hello, World!'

# Run the application if the script is run directly
if __name__ == '__main__':
    app.run()