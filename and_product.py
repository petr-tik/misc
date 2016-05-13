#!/usr/bin/env python

# https://www.hackerrank.com/challenges/and-product

def solve(start, finish):
    res = start
    for x in xrange(start + 1, finish + 1):
        res = res & x
    return res

T = int(raw_input())
for _ in xrange(T):
    start, finish = map(int, raw_input().split())
    print solve(start, finish)