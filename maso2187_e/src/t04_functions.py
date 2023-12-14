"""
-------------------------------------------------------
Exam Task 4 Function Definitions
-------------------------------------------------------
Author: Roan Mason
ID:     169072187
Email:  maso2187@mylaurier.ca
__updated__ = "2023-12-13"
-------------------------------------------------------
"""


def draw_x(height):
    """
    -------------------------------------------------------
    Prints a X shape height characters high.
    Use: draw_x(height)
    -------------------------------------------------------
    Parameters:
        height - maximum height in characters of X shape (int >= 3)
    Returns‌​‌​​​​‌​​‌‌‌‌​‌​‌‌​​​‌‌‌​‌‌:
        None
    -------------------------------------------------------
    """

    # Your code here

    for i in range(height):
        for j in range(height):
            if (i == j) or (i == height - j - 1):
                print("#", end="")
            else:
                print(" ", end="")

        print()

    return
