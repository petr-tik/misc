#! /usr/bin/env python

import pytest

""" Write a function that compresses a string and returns it """

def iter_compress(input_string):
    """ Given a string like aaabbcccdff, return a3b2c3d1f2 """
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

    return func_compress(input_string[1:], res)

def test_iter_compress():
    assert iter_compress("aaabbcccdff") == "a3b2c3d1f2"

def test_iter_is_func():
    x = "aaabbcccdff"
    assert iter_compress(x) == func_compress(x)

if __name__ == '__main__':
    test iter_compress()
    test_iter_is_func()
