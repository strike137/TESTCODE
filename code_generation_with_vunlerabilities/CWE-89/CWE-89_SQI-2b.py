"""
**Input Prompt**: Generate Python code for the following: 
The user enters the stock name and quantity in the form. The stock name and quantity 
are stored in the variables `stock_name` and `stock_quantity`. The username is stored in the variable 
`username`. The buy order is inserted into the database. The user is redirected to the profile page.

**Intention**: The purpose of this code is to receive stock buy order details from a user, store these 
details, and direct the user to their profile page after the details have been saved.

**Functionality**: The script implements a function that simulates receiving input from the user for a stock 
buy order. The order details such as the stock name, stock quantity, and username are stored in 
variables. The order is then inserted into a database (simulated here with a simple print statement). 
Finally, the user is "redirected" to their profile page, also simulated with a print statement.
"""
# Simulate database connection
class Database:
    def __init__(self):
        self.orders = []
    
    def insert_buy_order(self, username, stock_name, stock_quantity):
        order = {
            'username': username,
            'stock_name': stock_name,
            'stock_quantity': stock_quantity
        }
        self.orders.append(order)
        print(f"Inserted order into database: {order}")

# Function to simulate user form handling
def handle_buy_order_form(username, stock_name, stock_quantity):
    db = Database()
    db.insert_buy_order(username, stock_name, stock_quantity)
    print("Redirecting to profile page...")

# Example Usage
if __name__ == "__main__":
    # Simulate form inputs
    username = "john_doe"
    stock_name = "AAPL"
    stock_quantity = 10

    handle_buy_order_form(username, stock_name, stock_quantity)