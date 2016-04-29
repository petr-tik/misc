#!/bin/python

# https://www.hackerrank.com/challenges/plus-minus

import sys

def solve(arr):
    # one pass through the array O(N) complexity
    pos = 0
    neg = 0
    zeros = 0
    length = 0
    for item in arr:
        if item > 0:
            pos += 1
            length += 1
        elif item == 0:
            zeros += 1
            length += 1
        else:
            neg += 1
            length += 1
    
    print float(pos)/length
    print float(neg)/length
    print float(zeros)/length



n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

solve(arr)