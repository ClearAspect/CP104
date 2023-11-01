"""
-------------------------------------------------------
Midterm B Task 1 Function Definitions
-------------------------------------------------------
Author: Roan Mason
ID:     169072187
Email:  maso2187@mylaurier.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""
# Constants

# your constants here
NICKEL_AMOUNT = 5
DIME_AMOUNT = 10
QUATER_AMOUNT = 25
LOONIE_AMOUNT = 100

def minimal_change(cents):
    """
    -------------------------------------------------------
    Breaks down cents into a minimal number of coins.
    The change can be:
        loonies - coins worth 100 cents
        quarters - coins worth 25 cents
        dimes - coins worth 10 cents
        nickels - coins worth 5 cents
    Use: loonies, quarters, dimes, nickels = minimal_change(cents)
    -------------------------------------------------------
    Parameters:
        cents - number of cents (int >= 0)
    Returns‌​‌​​​​‌​​‌‌‌‌​‌​‌‌​​​‌‌‌​‌‌:
        loonies - number of loonies ($1 coins) (int)
        quarters - number of quarters (25 cent coins) (int)
        dimes - number of dimes (10 cent coins) (int)
        nickels - number of nickels (5 cent coins) (int)
    -------------------------------------------------------
    """

    # your code here
    loonies = cents // LOONIE_AMOUNT
    cents = cents % LOONIE_AMOUNT
    
    quaters = cents // QUATER_AMOUNT
    cents = cents % QUATER_AMOUNT
    
    dimes = cents // DIME_AMOUNT
    cents = cents % DIME_AMOUNT
    
    nickels = cents // NICKEL_AMOUNT
    cents = cents % NICKEL_AMOUNT
    
    return (loonies, quaters, dimes, nickels)
