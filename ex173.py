"""This module contains a code example related to

The Python Workbook, 2nd Edition
by Ben Stephenson
http://thinkpython2.com

Copyright 2020 Giuseppe Marcucci

License: http://creativecommons.org/licenses/by/4.0/
"""

total = 0.0


def total_the_values():
    global total
    end_input = False
    input_line: str = input("Insert a value (blank line to finish):")
    print('input_line *'+input_line+'*')
    if input_line == '':
        return total
    else:
        total = 1
        total += total_the_values()
        return total


res = total_the_values()
print("The total is: {}".format(res))