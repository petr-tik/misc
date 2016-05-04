#!/usr/bin/env python 

# https://www.hackerrank.com/challenges/maximizing-xor


def dec_to_binary(num):
    # given a dec number between 1 and 1000, 
    # convert to binary string of constant length regardless of dec value
    if num > 1000:
        print "can't do numbers over 1000"
    else:
        num_bin = bin(num)[2:]
        full_num = '0'*(10 - len(num_bin)) + num_bin
        return full_num

def maximise_xor(left, right):
    left_bin = dec_to_binary(left)
    right_bin = dec_to_binary(right)
    res = []
    for idx, left_char in enumerate(left_bin):
        if left_char == right_bin[idx]:
            res.append('0')
        else:
            res.append('1')
    return int("".join(res), 2)

def solve(left, right):
    lower_bound = min(left, right)
    upper_bound = max(left, right)
    answer = 0 
    for value1 in xrange(lower_bound, upper_bound + 1):
        for value2 in xrange(lower_bound, upper_bound + 1):
            maximise_xor_value = maximise_xor(value1, value2)
            if maximise_xor_value > answer:
                answer = maximise_xor_value
    return answer

print solve(10, 15)
