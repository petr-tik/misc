#! usr/bin/env/ python

# https://www.hackerrank.com/challenges/sherlock-and-array

"""
need to generate numbers from threes of 5's or fives of 3's 

the greatest decent number has as many fives as possible, then as many threes as possible
given N, iterate fives from N to 0, and threes from 0 to N.

As soon as you have a combinations of fives and threes occuring 3x and 5x times, 
make a number with all the 5s at the beginning followed by all the threes. 

If no such number exists, -1 is the answer

"""

def make_decent(N):
    "given N generate the largest decent number of N digits"
    fives = N
    for fives in xrange(N, -1, -1):
        threes = N - fives
        if fives % 3 == 0 and threes % 5 == 0:
            res = ''.join([fives*'5', threes*'3'])
            # all 5s followed by all 3s
            return int(res)
    # if nothing, then -1
    return -1

def solve():
    N = int(raw_input())
    print make_decent(N)

## HackerRank boilerplate

t = int(raw_input().strip())
for a0 in xrange(t):
    solve()