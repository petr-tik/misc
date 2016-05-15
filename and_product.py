#!/usr/bin/env python

# https://www.hackerrank.com/challenges/and-product
from math import log, modf

def dec_to_binary(num):
    # given a dec number between 1 and 2**32, 
    # convert to binary string of constant length regardless of dec value
    num_bin = bin(num)[2:]
    full_num = '0'*(32 - len(num_bin)) + num_bin
    return full_num

def solve(start, finish):
    # if start with zero or numbers are different powers of 2, 
    # return 0
    if start == 0 or modf(log(start, 2))[1] != modf(log(finish, 2))[1]:
        return 0

    # make a list of bit chars for each start and finish
    start_list = list(dec_to_binary(start))
    finish_list = list(dec_to_binary(finish))
    # result array holding '0' for now
    res = ['0' for _ in xrange(32)]
    # starting from the first char
    idx = 0
    while idx < 32:
        # compare 
        if start_list[idx] == finish_list[idx]:
            res[idx] = start_list[idx]
            idx += 1
            continue
        # as soon as you get to 2 different bits, from then on, 
        # bits will differ in the range
        # the result array already has 0s, so set idx=32 and stop the while loop
        # eg
        # 37 = 100001
        # 63 = 111111
        # &  = 100000 - first bits match, but as soon as they differ,
        # we know there will be 0s in those positions somewhere in our range
        else:
            idx = 32

    return int(''.join(res), 2)

"""
T = int(raw_input())
for _ in xrange(T):
    start, finish = map(int, raw_input().split())
    print solve(start, finish)
    """
