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

def calculate_monthly_payment(p: float, n: int, i: float) -> float:
    """
    -------------------------------------------------------
    description
    Use: Calculates the monthly payment of a mortgage in the US
    -------------------------------------------------------
    Parameters:
        p - principal value (float)
        n - number of payments (int)
        i - interest rate per month (float)
    Returns:
        The monthly payment (float)
    ------------------------------------------------------
    """

    monthly_payment = p * ((i*(pow((1+i),n))) / (pow((1+i),n) - 1))
    return monthly_payment

# Get Principal
principal = float(input("Mortgage principal ($): "))

# Get the number of years and convert it to number of payments
number_of_years = int(input("Number of years: "))
number_of_payments = number_of_years*12

# Get the % of interest and convert it to interest payed per month
interest = float(input("Yearly interest rate (%): "))
interest = interest/100/12

monthly_payment = calculate_monthly_payment(principal, number_of_payments, interest)

print("The monthly payments are: $", monthly_payment)
