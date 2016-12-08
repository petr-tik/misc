#! /usr/bin/env python

# https://www.hackerrank.com/challenges/unbounded-knapsack

considered = {}


def recur_solve(cur_value, arr, k, considered):
    """ Recursive solution. Takes cur_value, array, k and 
    already considereed hashmap (for memoization). """
    # memoization - if already solved, use the solution
    if cur_value in considered:
        return considered[cur_value]

    # optimisation hacks
    # you can use the numbers as many times as possible, so once you have:
    # 1 or a multiple of k, you are good
    if 1 in arr or any(k % item == 0 for item in arr):
        return k

    if cur_value == k:
        return cur_value

    temp = cur_value
    # for the value already calculated, try adding every number from array
    for item in arr:
        if cur_value + item <= k:  # once the running total is greater than k, stop
            res = recur_solve(cur_value + item, arr, k, considered)
            # the maximum you can get starting at cur_value is
            temp = max(temp, res)

    # now that temp is the maximum it can be, add it to a hashmap
    considered[cur_value] = temp
    return temp

# HackerRank boilerplate
"""    
T = int(raw_input())
for _ in xrange(T):
    n, k = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    considered = dict()
    print recur_solve(0, arr, k, considered)"""

print recur_solve(0, [4, 8, 12, 16], 5, considered)
