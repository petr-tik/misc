#! /usr/bin/env/python3

from collections import namedtuple, defaultdict
import string

""" Notes from reading fluent python. The book uses python3 and so will I. 
Covered so far:
   slicing
   tuples
"""

# Slices

TwoStep = slice(None, None, 2)
reverse_slice = slice(None, None, -1)
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
# namedtuple treats the string and splits it across whitespace
# "name age job salary".split()


first_record = DB_Record("john", 25, "journalist", 25000)
print(first_record)
second_rec = DB_Record("bob", 30, "jobless", 0)

# strings


""" dicts and sets """


def zero_func_for_anagram():
    """ define a callable i.e. a function that returns a value 
    that will be used when defaultdict doesn't find key """
    return 0

anagram_dict = defaultdict(lambda: 0)
# use a lambda func or zero_func_for_anagram

word = "lalalalsd"

# more pythonic than below - 2 lines, using a builtin type
for char in word:
    anagram_dict[char] += 1
print(anagram_dict)

plain_dict = {}
# instead of
for char in word:
    if plain_dict.has_key(char):
        plain_dict[char] += 1
    else:
        plain_dict[char] = 1


# to collect lists of indices, where a char appears
# use list()
char_idx_dict = defaultdict(list)  # if missing, start a list at key

for idx, char in enumerate(word):
    char_idx_dict[char].append(idx)

print(char_idx_dict)
""" functions """


def ex_func():
    """ docstring """
    x = 5  # comment 0
    # comment 1
    return None

print(ex_func.__doc__)
print(inspect.getcomments(ex_func))


# inspecting and disassembling

import dis
import inspect

""" dis is a builtin module for exploring/disassembling python bytecode
Interesting methods include:
     code_info - given a method/func/code
     dis - disassemlber a class/method/func
 """

for line in dis.code_info(ex_func).split("\n"):
    print(line)


""" Decorators 
2 decorators are in functools:
singledespatch - like different func bodies for different argument types
lru_cache - least-recently used cache - if maxsize=None grows without limit and stores returns from different function calls. typed=(default False) will tell between float 3.0 and int 3 and store results separately. This is good, but also shows the weakness switching between static and dynamic typing paradigm in one language

