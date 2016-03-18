#! usr/bin/env python

# https://www.hackerrank.com/contests/zenhacks/challenges/candy-shop

import sys

N = int(raw_input().strip())
coins = [1, 2, 5, 10, 20, 50, 100]
distr = []
res = 0

def solve(NUMBER):
    if NUMBER == 0:
        global res 
        res += 1
        return

    for x in coins:
        if x <= NUMBER and (not distr or x >= distr[-1]):
            distr.append(x)
            solve(NUMBER - x)
            distr.pop()

solve(N)
print res