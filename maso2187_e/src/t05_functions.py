"""
-------------------------------------------------------
Exam Task 5 Function Definitions
-------------------------------------------------------
Author: Roan Mason
ID:     169072187
Email:  maso2187@mylaurier.ca
__updated__ = "2023-12-13"
-------------------------------------------------------
"""


def fill_matrix(fh_in, rows, cols):
    """
    -------------------------------------------------------
    Creates a rows by cols 2D list of integers filled with
    space-separated integers from f_in. If f_in does not have enough values,
    fill the remaining slots with 0s. If f_in has too many values,
    the excess values are ignored.
    Use: matrix = fill_matrix(fh_in, rows, cols)
    -------------------------------------------------------
    Parameters:
        fh_in - the integers file to process (file handle - already open for reading)
        rows - rows in matrix (int > 0)
        cols - columns in matrix (int > 0)
    Returns‌​‌​​​​‌​​‌‌‌‌​‌​‌‌​​​‌‌‌​‌‌:
        matrix - a 2D list of integers (2D list of int)
    -------------------------------------------------------
    """

    # Your code here
    
    matrix = []
    
    line = fh_in.readline()
    current_line = line.split(" ")
    current_line_len = len(current_line)
    count = 0
    
    for i in range(rows):
        
        sub_matrix = []
        for j in range(cols):
            if (count >= current_line_len):
                line = fh_in.readline()
                current_line = line.split(" ")
                current_line_len = len(current_line)
                count = 0
            if (line == ""):
                sub_matrix.append(0)
            else:
                sub_matrix.append(int(current_line[count]))
                count += 1

            
                    
        matrix.append(sub_matrix)
            
            
                
            

    return matrix
