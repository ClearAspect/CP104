"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2023-10-03"
-------------------------------------------------------
"""


# Imports

# Constants
ANNUAL_TAX = 0.185

total_sales = float(input("Enter the total sales: $"))
tax = total_sales * ANNUAL_TAX

print(f"""
Projected Tax Report
--------------------------
Total Sales:    $ {total_sales:,.2f}
Annual Tax:     % {ANNUAL_TAX*100:,.2f}
--------------------------
Tax:            $  {tax:,.2f}""")