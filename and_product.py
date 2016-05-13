#!/usr/bin/env python

# https://www.hackerrank.com/challenges/and-product

def solve(start, finish):
    arr = [x for x in xrange(start, finish + 1)]
    return reduce(lambda x,y: x&y, arr)

T = int(raw_input())
for _ in xrange(T):
    start, finish = map(int, raw_input().split())
    print solve(start, finish)