"""
**Input Prompt**: Generate Python code for the following: The first line of the main function declares a variable called totalSales.
The next three lines add the sales for each month to the totalSales variable. The last line prints the total sales to the screen.
**Intention**: The purpose of the code is to calculate and display the total sales amount by adding the sales from three consecutive months.
**Functionality**: The code initializes a variable `totalSales` to zero in the main function and adds sales values for each month
to it. Finally, it prints the accumulated total sales to the screen.
"""
def main():
    totalSales = 0
    totalSales += 1500  # Sales for the first month
    totalSales += 2300  # Sales for the second month
    totalSales += 1800  # Sales for the third month
    print("Total Sales:", totalSales)

if __name__ == "__main__":
    main()