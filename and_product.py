#!/usr/bin/env python

# https://www.hackerrank.com/challenges/and-product
from math import log, modf

INT_LENGTH = 32


def dec_to_binary(num):
    """ given a decimal number between 1 and 2**32
    return a string of length 32 with its binary value """
    num_bin = bin(num)[2:]
    full_num = '0' * (INT_LENGTH - len(num_bin)) + num_bin
    return full_num


def solve(start, finish):
    """
    as soon as you get to 2 different bits, from then on,
    bits will differ in the range
    break out of the while loop by setting idx=32
    eg.
        37 = 100001
        63 = 111111
       &   = 100000 - first bits match, but as soon as they differ,
    we know there will be 0s in those positions somewhere in our range
    """

    # if start with zero or numbers are different powers of 2,
    # return 0
    if start == 0 or modf(log(start, 2))[1] != modf(log(finish, 2))[1]:
        return 0

    # make a list of bit chars for each start and finish
    start_bin = dec_to_binary(start)
    finish_bin = dec_to_binary(finish)
    # result array holding '0's for now
    res = ['0' for _ in xrange(INT_LENGTH)]
    # starting from the first char
    idx = 0
    while idx < INT_LENGTH:
        # compare
        if start_bin[idx] == finish_bin[idx]:
            res[idx] = start_bin[idx]
            idx += 1
            continue

        else:
            idx = INT_LENGTH

    return int(''.join(res), 2)


"""
T = int(raw_input())
for _ in xrange(T):
    start, finish = map(int, raw_input().split())
    print solve(start, finish)
"""
