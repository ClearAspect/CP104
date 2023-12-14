"""
-------------------------------------------------------
Exam Task 1 Function Definitions
-------------------------------------------------------
Author: Roan Mason
ID:     169072187
Email:  maso2187@mylaurier.ca
__updated__ = "2023-08-25"
-------------------------------------------------------
"""


def even_avg(values):
    """
    -------------------------------------------------------
    Returns the average (integer, rounded down) of all even numbers
    in values. If values has no even numbers, the average is 0.
    Use: ea = even_avg(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns‌​‌​​​​‌​​‌‌‌‌​‌​‌‌​​​‌‌‌​‌‌:
        ea - the average of the even numbers in values (int)
    -------------------------------------------------------
    """

    # your code here

    valuesLen = len(values)
    totalEven = 0
    count = 0

    for i in range(valuesLen):
        if values[i] % 2 == 0:
            totalEven += values[i]
            count += 1

    if count == 0:
        return 0

    average = int(totalEven / count)
    return average
