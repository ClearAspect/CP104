"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2023-11-04"
-------------------------------------------------------
"""
# Imports

# Constants

def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    product = 1
    for i in range(1, number + 1):
        product *= i
    return product

def calories_treadmill(per_min, minutes):
    """
    -------------------------------------------------------
    calories_treadmill prints a table of the number of calories burned every five minutes
    given the number of calories burned per minute (per_min) an the total number of minutes
    run (minutes). Align the results and print with 1 decimal accuracy for the calories burned
    as shown in the example execution.
    Use: calories_treadmill(per_min, minutes)
    -------------------------------------------------------
    Parameters:
        per_min - calories burned per minute (float > 0)
        minutes - total number of minutes (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(5, minutes + 1, 5):
        calories = i * per_min
        print(f"{i:3}{calories:>6.1f}")
    return

def arrow_up(rows):
    """
    -------------------------------------------------------
    takes an integer parameter and prints a arrow of # characters pointing up.
    example
       #
      # #
     #   #
    #     #
    Use: arrow_up(rows)
    -------------------------------------------------------
    Parameters:
        rows - number of rows (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """

    print(f"{'#': >{rows}}")
    for i in range(1, rows):
        print(f"{'#': >{rows - i}}", end='')
        print(f"{'#': >{i + i}}")


    """Another way to do it"""
    # for i in range(1, rows + 1):
    #     if i == 1:
    #         print(f"{' ' * (rows - i)}{'#'}")
    #     else:
    #         print(f"{' ' * (rows - i)}{'#'}{' ' * ((i - 1)+(i-2))}{'#'}")

    return

def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """

    print(f"{' ':7}", end="")
    for i in range(start_num, stop_num + 1):
        print(f"{i:5}", end="")
    print()

    print(f"{' ':7}{'-':-^{5*(stop_num - start_num + 1)}}")

    for i in range(start_num, stop_num + 1):
        print(f"{i:5} |", end="")
        for j in range(start_num, stop_num + 1):
            print(f"{i * j:5}", end="")
        print()
    return


def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(start, start + (increment * count), increment):
        total += i
    return total
