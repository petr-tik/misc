#! usr/bin/env python

# https://www.hackerrank.com/contests/zenhacks/challenges/candy-shop

import sys

N = int(raw_input().strip())
coins = [1, 2, 5, 10, 20, 50, 100]
distr = []
cache = [[-1 for _ in coins] for _ in xrange(N + 1)] 

def solve(NUMBER, start_pos):
    # check if the value has been calculated
    if cache[NUMBER][start_pos] != -1:
        return cache[NUMBER][start_pos]
    
    res = 0

    if NUMBER == 0:
        res = 1

    else:
        for i in xrange(start_pos, len(coins)):
            if coins[i] <= NUMBER:
                res += solve(NUMBER - coins[i], i)
            else:
                break
    
    cache[NUMBER][start_pos] = res
    return res

print solve(250, 0)
