#! /usr/bin/env/python3

from collections import namedtuple
import string

""" Notes from reading fluent python. The book uses python3 and so will I. 
Covered so far:
   slicing
   tuples
"""

# Slices

TwoStep = slice(None, None, 2)
# create a separate class object with start, stop and step parameters.
# this is why reversing a list is sometimes a [::-1] - it's a step of -1
# with default start and stop vals

big_list = [x for x in range(100)]
big_string = string.ascii_lowercase

print(big_string[TwoStep])  # works on strings
print(big_list[TwoStep])  # and lists
# use the slice to call the respective indices of the iterable object


# Named Tuples

DB_Record = namedtuple('Record', "name age job salary")
# can take a string of args separated by whitespace

first_record = DB_Record("john", 25, "journalist", 25000)
print(first_record)
second_rec = DB_Record("bob", 30, "jobless", 0)
