#!/bin/python

import sys

# https://www.hackerrank.com/challenges/time-conversion

def solve(s):
    hours = int(s[:2])
    dimension = s[-2:]
    if dimension == 'AM':
        if hours == 12:
            res = "00:{}".format(s[3:-2])
       	else:
		    res = s[:-2]
    else:
        if hours == 12:
            res = s[:-2]
        else:
            res = "{}:{}".format(hours + 12, s[3:-2])
    print res
    

time = raw_input().strip()
solve(time)
