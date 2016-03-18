#! usr/bin/env python

# https://www.hackerrank.com/contests/zenhacks/challenges/candy-shop

import sys
from sets import Set

N = int(raw_input().strip())
coins = [1, 2, 5, 10, 20, 50, 100]
distr = []
final_solution = Set()

def solve(NUMBER):
    if NUMBER == 0:
        distr_copy = [x for x in distr]
        distr_copy.sort()
        res = ""
        for x in distr_copy:
            res += str(x)
        final_solution.add(res)
        return

    for x in coins:
        if x <= NUMBER:
            distr.append(x)
            solve(NUMBER - x)
            distr.pop()
    
    
solve(N)
print len(final_solution)