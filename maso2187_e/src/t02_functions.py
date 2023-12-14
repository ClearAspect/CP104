"""
-------------------------------------------------------
Exam Task 2 Function Definitions
-------------------------------------------------------
Author: Roan Mason
ID:     169072187
Email:  maso2187@mylaurier.ca
__updated__ = "2023-08-25"
-------------------------------------------------------
"""
# Constants

# Your constants here


def rainfall():
    """
    -------------------------------------------------------
    Asks the user for daily rainfall (in mm) from the keyboard.
    The function stops asking for rainfall when the user enters -1.
    The function returns:
        the total number of dry_days days (rainfall lower than 4mm)
        the total number of damp_days days (rainfall 4mm - 8mm)
        the total number of wet_days days (rainfall greater than 8mm)
        the average rainfall for all days (rounded down)
    Do all inputs and calculations in integer.
    Use: dry_days, damp_days, wet_days, avg = rainfall()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌‌‌​‌​‌‌​​​‌‌‌​‌‌:
        dry_days - number of dry_days days (int)
        damp_days - number of damp_days days (int)
        wet_days - number of wet_days days (int)
        avg - average rainfall of all days (int)
    -------------------------------------------------------
    """

    # your code here

    dry_days = 0
    damp_days = 0
    wet_days = 0
    avg = 0
    count = 0;
    
    rainamount = int(input("Rainfall mm (-1 to stop): "))
    while (rainamount != -1):
        avg += rainamount
        count += 1
        if (rainamount < 4):
            dry_days += 1
        elif (rainamount <= 8):
            damp_days += 1
        elif (rainamount > 8):
            wet_days += 1
        
        rainamount = int(input("Rainfall mm (-1 to stop): "))
    
    avg = int(avg / count)
    
    return dry_days, damp_days, wet_days, avg