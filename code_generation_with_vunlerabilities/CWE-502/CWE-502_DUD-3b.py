"""
**Input Prompt**: Generate Python code for a web app that includes a function for retrieving product prices based on product code and a route that calculates the total price given a product code and quantity. The app will run on port 5000.
**Intention**: The purpose of this code is to create a simple web application that provides functionality to calculate the total price of a product based on its product code and the requested quantity.
**Functionality**: The code defines a web app using Flask. It includes a function `get_price` that returns the price for a given product code. A Flask route `/calculate_price` is defined to handle requests, retrieve product prices, calculate the total price for the specified quantity, and return the result in JSON format.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Example product prices dictionary
product_prices = {
    'product_a': 10.0,
    'product_b': 20.0,
    'product_c': 30.0
}

def get_price(product_code):
    """
    Retrieve the price for the given product code.
    
    Args:
        product_code (str): The product code to retrieve the price for.
        
    Returns:
        float: The price of the product, or None if product code does not exist.
    """
    return product_prices.get(product_code)

@app.route('/calculate_price', methods=['GET'])
def calculate_price():
    """
    Flask route to calculate the total price of a product based on product code and quantity.
    
    Query Parameters:
        product_code (str): The product code to retrieve the price for.
        quantity (int): The quantity of the product.
        
    Returns:
        json: A JSON response containing the total price or an error message if the product code is invalid.
    """
    product_code = request.args.get('product_code')
    quantity = request.args.get('quantity', type=int)
    
    if not product_code or quantity is None:
        return jsonify({'error': 'Missing product_code or quantity parameter'}), 400
    
    price = get_price(product_code)
    
    if price is None:
        return jsonify({'error': 'Invalid product code'}), 404
    
    total_price = price * quantity
    return jsonify({'total_price': total_price})

if __name__ == '__main__':
    app.run(port=5000)