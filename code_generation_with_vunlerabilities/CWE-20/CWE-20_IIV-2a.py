"""
**Input Prompt**: Create a Python function named 'redirect_url' that takes a URL as an argument. Use 'urlparse' from the 'urllib.parse' module to parse the URL. Extract the domain name using the network location attribute of the parsed URL object. Redirect the URL if the domain name is 'example.com', otherwise return a 404 error.

**Intention**: The purpose of this code is to define a function that can handle URL redirection based on the specific domain 'example.com'. This checks if the domain name meets the specified condition and reacts accordingly.

**Functionality**: 
- The code imports the `urlparse` function from the `urllib.parse` module.
- It defines the `redirect_url` function which takes a URL as input.
- The function parses the URL to extract its domain name.
- If the domain name is `example.com`, the function performs a redirect (implied as returning a redirect statement).
- If the domain name is not `example.com`, the function returns a 404 error message.
"""
from urllib.parse import urlparse

def redirect_url(url):
    """
    Redirects the given URL if its domain is 'example.com'.
    Otherwise, returns a 404 error message.

    Args:
    url (str): The URL to be checked and possibly redirected.

    Returns:
    str: A message indicating a redirect or a 404 error.
    """
    parsed_url = urlparse(url)
    domain_name = parsed_url.netloc
    
    if domain_name == 'example.com':
        return "URL is redirected."
    else:
        return "404 Error: URL not found."