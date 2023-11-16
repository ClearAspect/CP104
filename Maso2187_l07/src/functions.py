"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2023-11-03"
-------------------------------------------------------
"""
# Imports
from random import randint


# Constants
OVERTIME = 40
OVERTIME_RATE = 1.5
TAX_RATE = 0.03625


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    number = randint(1, high)
    guess = int(input("Guess: "))
    count = 1
    while guess != number:
        count += 1

        if guess < number:
            print("Too low, try again.")
        else:
            print("Too high, try again.")
        guess = int(input("Guess: "))

    print("Congratulations - good guess!")
    print("You made", count, "guesses.")
    return count


def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    power = 0
    saved_num = 2**power
    saved_difference = float('inf')
    current_difference = abs(target - saved_num)
    while current_difference <= saved_difference:
        saved_difference = current_difference
        power += 1
        saved_num = 2**power
        current_difference = abs(target - saved_num)

    return 2**(power-1)


def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    number = -1
    while number < 0:
        number = float(input("First positive value: "))

    minimum = number
    maximum = number
    total = number
    count = 1
    number = float(input("Next positive value: "))
    while number >= 0:
        total += number
        count += 1

        if number < minimum:
            minimum = number
        elif number > maximum:
            maximum = number

        number = float(input("Next positive value: "))

    average = total / count
    return minimum, maximum, total, average


def num_categories():
    """
    -------------------------------------------------------
    Asks a user to enter a series of numbers, then counts and returns
    how may positives, negatives, and zeroes there are.
    Stop processing values when the user enters -999.
    Use: negatives, zeroes, positives = num_categories()
    -------------------------------------------------------
    Returns:
        negatives - number of negative values (int)
        zeroes - number of zero values (int)
        positives - number of positive values (int)
    ------------------------------------------------------
    """
    number = float(input("First value: "))
    negatives = 0
    zeroes = 0
    positives = 0
    while number != -999:
        if number < 0:
            negatives += 1
        elif number == 0:
            zeroes += 1
        else:
            positives += 1
        number = float(input("Next value: "))

    return negatives, zeroes, positives

def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    day = 1
    b_total = 0
    l_total = 0
    s_total = 0
    total_cost = 0
    more = "Y"
    while more == "Y":
        print("For Day", day,"\n")
        b_cost = float(input("How much was breakfast? $"))
        l_cost = float(input("How much was lunch? $"))
        s_cost = float(input("How much was supper? $"))
        day_cost = b_cost + l_cost + s_cost
        print(f"Your total for the day was ${day_cost:.2f}")

        day += 1
        b_total += b_cost
        l_total += l_cost
        s_total += s_cost
        total_cost += day_cost
        more = input("\nWere you away another day (Y/N)? ")
        print()
    return b_total, l_total, s_total, total_cost


def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    employee_id = int(input("Employee ID: "))
    total = 0
    count = 0
    while employee_id != 0:
        wage = float(input("Hourly wage rate: "))
        hours = float(input("Hours worked: "))
        if hours > 40:
            overtime_hours = hours - OVERTIME
            overtime_pay = wage * OVERTIME_RATE * overtime_hours
            regular_pay = wage * OVERTIME
            gross_pay = regular_pay + overtime_pay
        else:
            gross_pay = wage * hours

        tax = gross_pay * TAX_RATE
        net_pay = gross_pay - tax
        print(f"Net payment for employee {employee_id}: ${net_pay:.2f}")
        total += net_pay
        count += 1
        employee_id = int(input("\nEmployee ID: "))

    average = total / count
    return total, average