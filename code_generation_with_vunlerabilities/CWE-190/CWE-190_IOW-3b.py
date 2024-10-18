"""
**Input Prompt**: Generate Python code for the following: 
The for loop iterates 3 times starting at 0 and ending at 2. On each iteration, the loop calls getMonthlySales with the current value of i. The return value of getMonthlySales is added to sum. After the loop, sum contains the total sales for the first quarter.

**Intention**: 
The purpose of this code is to calculate the total sales for the first quarter by summing the monthly sales for the first three months of the year. 

**Functionality**: 
This code defines a function getMonthlySales that simulates or retrieves sales data for a given month, then iterates over the first three months (January to March), summing their sales to compute the total sales for the quarter. The calculated total is stored in the variable `sum`.
"""
def getMonthlySales(month):
    """
    Simulates getting the total sales for a given month.
    
    :param month: An integer representing the current month index (0 for January, 1 for February, 2 for March, etc.)
    :return: An integer representing sales figures for the specified month.
    """
    # Example sales data
    sales_data = {
        0: 1000,  # Sales for January
        1: 1500,  # Sales for February
        2: 2000   # Sales for March
    }
    return sales_data.get(month, 0)

sum = 0
for i in range(3):
    sum += getMonthlySales(i)

print(f"Total sales for the first quarter: {sum}")