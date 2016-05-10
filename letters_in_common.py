#! /usr/bin/env python

# https://www.hackerrank.com/challenges/gem-stones
import string

def solve(alist):
    alph = string.lowercase
    shared = 0
    for char in alph:
        if all(char in x for x in alist):
            shared += 1 

    return shared


N = int(raw_input())
s = []
for _ in xrange(N):
    s.append(raw_input())
print solve(s)