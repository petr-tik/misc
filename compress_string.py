#! /usr/bin/env python

import pytest

"""
Write a function that compresses a string and returns it
eg. given a string like aaabbcccdff, return a3b2c3d1f2
"""


def iter_compress(input_string):
    """
    Takes input string as input, returns compressed string.

    Iterate over every character in input.
    if the char same as last counted char - increment its counter in the res array
    else: add {char}1 to the res array

    return res array as string
    """
    res = []
    for char in input_string:
        if not res or res[-1][0] != char:
            res.append("{}1".format(char))
            continue
        if res[-1][0] == char:
            count_of_last_char = int(res[-1][1])
            new_char_n_count = "{}{}".format(char, count_of_last_char + 1)
            res[-1] = new_char_n_count

    return "".join(res)


def func_compress(input_string, res=[]):
    """
    Recursive solution of compressing a string.
    Same idea as iterative, instead of iterating over the input_string
    pass the string and res array into the next recursive func call
    when string is empty, return contents of the array.
    """
    if input_string == "":
        outcome = format("".join(res))
        return outcome
    new_char = input_string[0]

    if not res or new_char != res[-1][0]:
        res.append("{}1".format(new_char))
    else:
        count_of_last_char = int(res[-1][1])
        new_char_n_count = "{}{}".format(new_char, count_of_last_char + 1)
        res[-1] = new_char_n_count

    # need to return the recursive function call
    # otherwise the function returns None
    return func_compress(input_string[1:], res)


def test_iter_compress():
    assert iter_compress("aaabbcccdff") == "a3b2c3d1f2"


def test_iter_is_func():
    x = "aaabbcccdff"
    assert iter_compress(x) == func_compress(x)

if __name__ == '__main__':
    test iter_compress()
    test_iter_is_func()
