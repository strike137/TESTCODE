"""
**Input Prompt**: Generate Python code for creating a web service function that takes an environment
argument, extracts a name parameter from a request, retrieves a template from the environment, renders
it with the name, and returns this rendered template as a response. Create a home function that uses
this service to return a rendered page.

**Intention**: The purpose of this code is to provide a clear implementation of a service function that 
renders a personalized template page based on a name provided in the request, using a specified environment.

**Functionality**: The 'render_response_from_env' function takes an environment object, retrieves a
name parameter from a hypothetical request, gets a template from the environment, renders this template
with the name, and returns the rendered template as a response. The 'home' function calls 
'render_response_from_env' with a predefined environment and returns the response it receives.
"""
def render_response_from_env(env):
    """
    Renders a template with a specified name from the request and returns it as the response.

    Args:
        env (object): An environment object containing templates.

    Returns:
        str: A rendered template string.
    """
    # Hypothetical request object
    request = {'name': 'World'}  # Example name parameter

    # Retrieve the 'name' parameter from the request
    name = request.get('name', 'Guest')  # Default to 'Guest' if not found

    # Fetch the template from the environment object
    template = env.get_template('welcome.html')

    # Render the template with the provided name
    rendered_template = template.render(name=name)

    # Return the rendered template
    return rendered_template

def home():
    """
    Calls the 'render_response_from_env' function with a sample environment and returns the result.

    Returns:
        str: The response obtained from 'render_response_from_env'.
    """
    # Sample environment object
    class Environment:
        def get_template(self, template_name):
            return Template(template_name)

    class Template:
        def __init__(self, template_name):
            self.template_name = template_name

        def render(self, name):
            return f"Welcome {name} to our service!"

    # Create an environment instance
    env = Environment()

    # Call the service function with the environment
    response = render_response_from_env(env)

    # Return the response
    return response

if __name__ == "__main__":
    # Execute home function and print the response
    print(home())