#! /usr/bin/env python

import pytest

""" Write a function that compresses a string and returns it """

def compress(input_string):
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


def test_compress():
    assert compress("aaabbcccdff") == "a3b2c3d1f2"

if __name__ == '__main__':
    print compress("aaabbcccdff")
    print compress("aaabbcccdff") == "a3b2c3d1f2"
    #test_compress()
