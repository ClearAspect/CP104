"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2023-09-14"
-------------------------------------------------------
"""
# Imports

# Constants
PROFIT_PERCENTAGE = 0.18

projected_sales = float(input("Enter projected annual sales: $"))

projected_profit = projected_sales * PROFIT_PERCENTAGE

print("The projected profit on sales of $",projected_sales," is $",projected_profit)
