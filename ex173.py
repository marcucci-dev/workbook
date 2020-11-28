"""This module contains a code example related to

The Python Workbook, 2nd Edition
by Ben Stephenson

Copyright 2020 Giuseppe Marcucci

License: http://creativecommons.org/licenses/by/4.0/
"""


def total_the_values():
    input_line: str = input("Insert a value (blank line to finish):")
    if input_line == '':
        return 0.0
    else:
        return float(input_line) + total_the_values()


res = total_the_values()
print("The total is: {}".format(res))