"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2023-11-20"
-------------------------------------------------------
"""
# Imports
from functions import customer_record

# Constants

fh = open("src/customers.txt", "r", encoding="utf-8")
print(customer_record(fh, 3))
