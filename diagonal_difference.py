#!/bin/python

import sys

# https://www.hackerrank.com/challenges/diagonal-difference

def solve(arr, N):
    "given an (NxN) matrix as array of arrays and N output the diagonal difference"
    primary = 0
    secondary = 0
    for idx in xrange(N):
        primary += arr[idx][idx]
        secondary += arr[idx][-1 - idx]
    return abs(primary - secondary)


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)

print solve(a, n)
