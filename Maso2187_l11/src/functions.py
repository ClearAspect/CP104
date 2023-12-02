"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2023-11-30"
-------------------------------------------------------
"""
# Imports
import random

# Constants


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if value_type == "float":
                row.append(random.uniform(low, high))
            elif value_type == "int":
                row.append(random.randint(low, high))
        matrix.append(row)
    return matrix


def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    rows = len(matrix)
    cols = len(matrix[0])

    print(f"{' ':2}", end="")
    for i in range(cols):
        print(f"{i:>7d}", end="")

    for i in range(rows):
        print("\n", end=f"{i:>2d}")
        for j in range(cols):
            if value_type == "float":
                print(f"{matrix[i][j]:>7.2f}", end="")
            elif value_type == "int":
                print(f"{matrix[i][j]:>7d}", end="")

    return


def matrix_stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
                Use: smallest, largest, total, average = matrix_stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    smallest = float("inf")
    largest = float("-inf")
    total = 0
    amount_of_nums = len(matrix) * len(matrix[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            total += matrix[i][j]
            if matrix[i][j] > largest:
                largest = matrix[i][j]
            if matrix[i][j] < smallest:
                smallest = matrix[i][j]

    average = total / amount_of_nums
    return smallest, largest, total, average
