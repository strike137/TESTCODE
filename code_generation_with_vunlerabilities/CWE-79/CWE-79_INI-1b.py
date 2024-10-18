"""
**Input Prompt**: Generate Python code for a function `http_hello_page` that handles an HTTP request and response. 
The function reads a username from the request and responds with "Hello [username]".

**Intention**: The purpose of this code is to define a function that processes an HTTP-like request by reading a username
from the request stream and returns a greeting to the client through the response stream.

**Functionality**: The function `http_hello_page` takes in a request and a response, reads the username from the request stream,
constructs a response message "Hello [username]", and writes this message to the response stream for the client to receive.
"""
def http_hello_page(request, response):
    """
    Processes the request to extract the username and sends back a personalized greeting.

    :param request: A file-like object that simulates the client's request stream containing the username.
    :param response: A file-like object where the response message will be written.
    """
    # Read the username from the request stream
    username = request.read().strip()

    # Construct the greeting
    greeting = f"Hello {username}"

    # Write the greeting to the response stream
    response.write(greeting)

# Example usage, assuming request and response are file-like objects:
# with open('request.txt', 'r') as req, open('response.txt', 'w') as res:
#     http_hello_page(req, res)