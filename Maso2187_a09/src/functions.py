"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
# Imports


# Constants


def func():
    """
    -------------------------------------------------------
    description
    Use:
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """


def file_top(file_handle, count):
    """
    -------------------------------------------------------
    Prints first count lines of file_handle. Line numbering starts at 0.
    If length of file is shorter than count, stops printing after
    last line of file.
    Use: file_top(file_handle, count)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
        count - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    counter = 0
    while counter < count:
        line = file_handle.readline()
        if line != "":
            print(line, end="")
            counter += 1
    return


def read_integers(file_handle):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: number_list = read_integers(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        number_list - a list of integers from file_handle (list of int)
    -------------------------------------------------------
    """
    number_list = []
    line = file_handle.readline()
    while line != "":
        line = line.strip().split(",")
        for i in line:
            if i.isdigit():
                number_list.append(int(i))
        line = file_handle.readline()
    return number_list


def file_statistics(file_handle):
    """
    -------------------------------------------------------
    Evaluates the contents of a file by counting upper-case letters,
    lower-case letters, digits, white-spaces (including end-of-line
    characters), and remaining characters.
    Use: ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        ucount - The number of upper-case letters in the file (int)
        lcount - The number of lower-case letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of white-space characters in the file (int)
        rcount - The number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    ucount = 0
    lcount = 0
    dcount = 0
    wcount = 0
    rcount = 0
    line = file_handle.readline()
    while line != "":
        for i in line:
            if i.isupper():
                ucount += 1
            elif i.islower():
                lcount += 1
            elif i.isdigit():
                dcount += 1
            elif i.isspace():
                wcount += 1
            else:
                rcount += 1
        line = file_handle.readline()
    return ucount, lcount, dcount, wcount, rcount


def line_numbering(fh_read, fh_write):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_write contain contents
    of fh_read where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: line_numbering(fh_read, fh_write)
    -------------------------------------------------------
    Parameters:
        fh_read - file to read (file - open for reading)
        fh_write - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    line = fh_read.readline()
    counter = 0
    while line != "":
        fh_write.write("[" + str(counter) + "] " + line)
        line = fh_read.readline()
        counter += 1
    return


def student_stats(file_handle):
    """
    -------------------------------------------------------
    Get information from a file of file_handle and grades.
    Use: l_id, h_id, avg = student_stats(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    l_id = ""
    h_id = ""
    highest_mark = float("-inf")
    lowest_mark = float("inf")
    total = 0
    count = 0
    line = file_handle.readline()
    while line != "":
        line = line.strip().split(",")
        if float(line[3]) > highest_mark:
            highest_mark = float(line[3])
            h_id = line[2]
        if float(line[3]) < lowest_mark:
            lowest_mark = float(line[3])
            l_id = line[2]
        total += float(line[3])
        count += 1
        line = file_handle.readline()
    avg = total / count
    return l_id, h_id, avg
