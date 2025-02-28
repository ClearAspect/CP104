"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2023-10-17"
-------------------------------------------------------
"""


# Imports

# Constants
ACC_GRAVITY = 9.8

# Age constants
INFANT_AGE = 3
KID_AGE = 10
ADULT_AGE = 18
SENIOR_AGE = 65

def get_weight(mass):
    """
    -------------------------------------------------------
    Describes a mass in terms of its weight. If its weight is > 1000 N,
    it is "heavy", less than 10 N it is "light", and "average" otherwise.
    weight = mass (kg)  acceleration due to gravity (9.8/m/s^2)
    Use: weight, message = get_weight(mass)
    -------------------------------------------------------
    Parameters:
        mass - mass of an object in kg (float > 0)
    Returns:
        weight - weight of an object in Newtons (float)
        message - description of weight of object (str)
    -------------------------------------------------------
    """
    weight = mass * ACC_GRAVITY
    if weight > 1000:
        message = "heavy"
    elif weight < 10:
        message = "light"
    else:
        message = "average"

    return weight, message


def is_leap(year) -> bool:
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    result = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    return result

def roman_numeral(n):
    """
    -------------------------------------------------------
    Convert 1-10 to Roman numerals.
    Use: numeral = roman_numeral(n)
    -------------------------------------------------------
    Parameters:
        n - number to convert to Roman numerals (int)
    Returns:
        numeral - Roman numeral version of n, None if n is not
          between 1 and 10 inclusive. (str)
    -------------------------------------------------------
    """
    if n == 1:
        numeral = "I"
    elif n == 2:
        numeral = "II"
    elif n == 3:
        numeral = "III"
    elif n == 4:
        numeral = "IV"
    elif n == 5:
        numeral = "V"
    elif n == 6:
        numeral = "VI"
    elif n == 7:
        numeral = "VII"
    elif n == 8:
        numeral = "VIII"
    elif n == 9:
        numeral = "IX"
    elif n == 10:
        numeral = "X"
    else:
        numeral = None

    return numeral

def quadrant(x, y):
    """
    -------------------------------------------------------
    Determines location on a plane of an x, y coordinate.
    Use: location = quadrant(x, y)
    -------------------------------------------------------
    Parameters:
        x - x coordinate on a Cartesian plane (float)
        y - y coordinate on a Cartesian plane (float)
    Returns:
        location - one of: 'Quadrant 1', 'Quadrant 2', 'Quadrant 3'
          'Quadrant 4', 'X-Axis', 'Y-Axis', 'Origin' (str)
    -------------------------------------------------------
    """
    if x == 0 and y == 0:
        location = "Origin"
    elif x == 0:
        location = "Y-Axis"
    elif y == 0:
        location = "X-Axis"
    elif x > 0 and y > 0:
        location = "Quadrant 1"
    elif x < 0 and y > 0:
        location = "Quadrant 2"
    elif x < 0 and y < 0:
        location = "Quadrant 3"
    elif x > 0 and y < 0:
        location = "Quadrant 4"
    else:
        location = None

    return location

def ticket():
    """
    -------------------------------------------------------
    School play ticket price calculation.
    Asks user for their age, and if necessary, if they are
    a student at the school. Prices:
        Infant (age < 3): $0
        Senior (age >= 65): $4.00
        Student (10 <= age < 18): $3.00
            Student of this school: $1.00
        Adult (18 <= age < 65): $5.00
        Kid (3 <= age < 10): $2.00
    Use: price = ticket()
    -------------------------------------------------------
    Returns:
        price - the price of one ticket (float)
    -------------------------------------------------------
    """
    age = int(input("How old are you?: "))
    if age < INFANT_AGE:
        price = 0
    elif age >= SENIOR_AGE:
        price = 4.00
    elif KID_AGE <= age < ADULT_AGE:
        student = input("Student (Y/N): ")
        if student == "Y":
            price = 1.00
        else:
            price = 3.00
    elif ADULT_AGE <= age < SENIOR_AGE:
        price = 5.00
    elif INFANT_AGE <= age < KID_AGE:
        price = 2.00
    else:
        price = None

    return price