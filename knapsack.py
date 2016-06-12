#! /usr/bin/env python

# https://www.hackerrank.com/challenges/unbounded-knapsack

def recur_solve(cur_value, arr, k):
    considered = dict()
    
    if 1 in arr or any(k % item == 0 for item in arr):
        return k

    if cur_value == k:
        return cur_value

    temp = cur_value
    for item in arr:
        if cur_value + item <= k:
            res = recur_solve(cur_value + item, arr, k)
            temp = max(temp, res)
            considered.a
    return temp 

print recur_solve(0, [3,6,9], 13)