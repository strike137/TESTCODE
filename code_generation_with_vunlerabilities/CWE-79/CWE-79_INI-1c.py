"""
**Input Prompt**: Generate Python code for the following:
The function http_hello_page takes in a request and a response. The request is a file stream that contains the request from the client. The response is a file stream that we can write to. The request contains the username that the client entered. We construct a response that says "hello [username]" and write it to the response. The response is sent back to the client.

**Intention**: The purpose of writing this code is to generate a Python function named `http_hello_page` that processes an HTTP-style request to extract a username and send a personalized greeting back to the client through a provided response stream.

**Functionality**: This code defines a function `http_hello_page` that reads from an input stream (request) to extract a username. It then constructs a greeting message "hello [username]" and writes the message to an output stream (response), which is meant to be sent back to the client.

"""
def http_hello_page(request, response):
    """
    Process a request to greet the user by username and write the greeting message to the response.

    Args:
        request: A file-like object from which the request data can be read.
        response: A file-like object to which the response message can be written.

    Returns:
        None
    """
    # Read the request data
    request_data = request.read()
    
    # Assume that the request data is formatted as a simple string 'username=<value>'
    # We extract the username by splitting the string
    username_key_value = request_data.strip().split('=')
    if len(username_key_value) != 2 or username_key_value[0] != 'username':
        response.write("Invalid request format.\n")
        return
    
    username = username_key_value[1]
    
    # Construct the response message
    greeting = f"hello {username}\n"
    
    # Write the response message to the response stream
    response.write(greeting)