#! /usr/bin/env python

# https://www.hackerrank.com/challenges/unbounded-knapsack

def recur_solve(cur_value, arr, k, considered):
    if cur_value in considered:
        return considered[cur_value]
    
    if 1 in arr or any(k % item == 0 for item in arr):
        return k

    if cur_value == k:
        return cur_value

    temp = cur_value
    for item in arr:
        if cur_value + item <= k:
            res = recur_solve(cur_value + item, arr, k, considered)
            temp = max(temp, res)
    
    considered[cur_value] = temp    
    return temp    
    
## HackerRank boilerplate    
T = int(raw_input())
for _ in xrange(T):
    n, k = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    considered = dict()
    print recur_solve(0, arr, k, considered)