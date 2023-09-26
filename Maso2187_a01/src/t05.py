"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2023-09-26"
-------------------------------------------------------
"""


# Imports

# Constants

principal = float(input("Principal: $"))
interest = float(input("Interest (%): "))
interest /= 100
years = int(input("Number of years: "))
compounds = int(input("Number of times interest compounded per year: "))

amount = principal*(1+(interest/compounds))**(years*compounds)

print("Balance: $",amount)