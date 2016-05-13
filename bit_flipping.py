#! /usr/bin/env python

# https://www.hackerrank.com/challenges/flipping-bits

def dec_to_binary(num):
    # given a dec number between 1 and 2**32, 
    # convert to binary string of constant length regardless of dec value
    num_bin = bin(num)[2:]
    full_num = '0'*(32 - len(num_bin)) + num_bin
    return full_num

def solve(number):
    # given a number in decimal form, convert to bin 
    # and output decimal value when bits have been flipped
    bin_string = dec_to_binary(number)
    res = []
    for char in bin_string:
        if char == '1':
            res.append('0')
        else:
            res.append('1')
    return int(''.join(res), 2)

### HackerRank boilerplate

T = int(raw_input())
for _ in xrange(T):
    number = int(raw_input())
    print solve(number)