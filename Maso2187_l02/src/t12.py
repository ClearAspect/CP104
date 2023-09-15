"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2023-09-14"
-------------------------------------------------------
"""
# Imports

# Constants
SECONDS_PER_DAY = 86400
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60


number_of_seconds = int(input("Enter the number of seconds: "))

number_of_days = number_of_seconds // SECONDS_PER_DAY
number_of_seconds -= SECONDS_PER_DAY * number_of_days

number_of_hours = number_of_seconds // SECONDS_PER_HOUR
number_of_seconds -= SECONDS_PER_HOUR * number_of_hours

number_of_minutes = number_of_seconds // SECONDS_PER_MINUTE
number_of_seconds -= 60*number_of_minutes

print("Days:",number_of_days,"Hours:",number_of_hours,"Minutes:",number_of_minutes,"Seconds:",number_of_seconds)
