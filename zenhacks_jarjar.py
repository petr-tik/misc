#!/usr/bin/env python

# https://www.hackerrank.com/contests/zenhacks/challenges/pairing

N = int(raw_input())
def solve(Num):
    res = {}
    answer = 0
    for x in xrange(Num):
        shoe = raw_input()
        res_k = shoe[:-2]
        foot = shoe[-1:]
        if not res.has_key(res_k):
            res[res_k] = [foot]
        else:
            res[res_k].append(foot)
    for k in res:
        lefts = res[k].count('L')
        rights = res[k].count('R')
        answer += min(lefts, rights)

    return answer

print solve(N)

