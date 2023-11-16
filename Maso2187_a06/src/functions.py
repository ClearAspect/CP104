"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2023-11-11"
-------------------------------------------------------
"""


# Imports

# Constants


def total_wins():
    """
    -------------------------------------------------------
    total_wins takes no parameters and asks the user to enter a series of strings that represent the output of a
    game with a loop. The user should enter an empty string to signal the end of the series.
    After all strings have been entered, the function returns two numbers representing how many times the string
    "purple" appeared in the input and how many times the string "gold" appeared in the input.
    Use: total_wins()
    -------------------------------------------------------
    Parameters:
        None
    Returns:
        purples - number of purples (int)
        golds - number of golds (int)
    ------------------------------------------------------
    """
    purples = 0
    golds = 0
    user_input = input("Enter the winning team: ")
    while user_input != "":
        if user_input == "purple":
            purples += 1
        elif user_input == "gold":
            golds += 1
        user_input = input("Enter the winning team: ")

    return purples, golds

def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number using a while loop.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    prime = True
    i = 2
    while i < number:
        if number % i == 0:
            prime = False
        i += 1
    return prime

def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    print(f"Principal: {principal_amount:,.2f}")
    print(f"Interest Rate: {interest_rate:.2f}%")
    print(f"Monthly Payment: {payment:,.2f}")
    print("----------------------------------")
    print("Month Interest   Payment   Balance")
    print("----------------------------------")
    balance = principal_amount
    month = 1
    while balance > 0:
        interest = balance * (interest_rate / 100 / 12)
        balance += interest
        balance -= payment

        if balance < 0:
            payment = balance + payment
            balance = 0
        print(f"{month:5d} {interest:8.2f} {payment:9.2f} {balance:9.2f}")
        month += 1

    return

def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    digits = 0
    number = abs(number)
    while number > 0:
        number //= 10
        digits += 1
    return digits

def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """
    total = 0
    i = 1
    while i < number:
        if number % i == 0:
            total += i
        i += 1
    return total