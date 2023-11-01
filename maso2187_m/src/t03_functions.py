"""
-------------------------------------------------------
Midterm B Task 3 Function Definitions
-------------------------------------------------------
Author: Roan Mason
ID:     169072187
Email:  maso2187@mylaurier.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""
# Constants
FURNACE_BASE = 125.00
EXTRA_SERVICE = 25.00
DISCOUNT = 0.10

# your constants here


def servicing():
    """
    -------------------------------------------------------
    Determines the cost of getting a home furnace tune up. The cost is made up of:
        base cost: $125.00
        cost per extra service: $25.00
        VIP discount 10% only if:
            more than 1 extra service purchased
            and purchaser is a VIP
    The function must ask the user for these inputs.
    Use: cost = servicing()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌‌‌​‌​‌‌​​​‌‌‌​‌‌:
        cost - cost of getting a home furnace tune up based upon the base cost,
            the number of extra services purchased, and VIP discount
            if applicable (float)
    -------------------------------------------------------
    """

    # your code here
    number_of_services = int(input("How many extra services are you purchasing? "))
    cost = FURNACE_BASE
    cost += number_of_services * EXTRA_SERVICE

    
    if number_of_services > 1:        
        is_vip = input("Are you a VIP member (Y/N)? ")
        if is_vip == "Y":
            cost *= (1-DISCOUNT)

    return cost
