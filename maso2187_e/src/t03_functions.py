"""
-------------------------------------------------------
Exam Task 3 Function Definitions
-------------------------------------------------------
Author: Roan Mason
ID:     169072187
Email:  maso2187@mylaurier.ca
__updated__ = "2023-12-13"
-------------------------------------------------------
"""


def upper_vowels(string):
    """
    -------------------------------------------------------
    Converts vowels in a string to upper-case, all other 
    letters to lower-case. Non letters are left unchanged.
    Vowels include: aeiou.
    Use: altered = upper_vowels(string)
    -------------------------------------------------------
    Parameters:
        string - string to process (str)
    Returns‌​‌​​​​‌​​‌‌‌‌​‌​‌‌​​​‌‌‌​‌‌:
        altered - the resulting string (str)
    -------------------------------------------------------
    """

    # Your code here

    altered = ""
    string = string.lower()
    for c in string:
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
            altered += c.upper()
        else:
            altered += c

    return altered
