#!/bin/python

# https://www.hackerrank.com/challenges/angry-professor

import sys

def is_cancelled(arrivals, threshold):
    # iterates over the array once
    on_time = 0
    for student_time in arrivals:
        if student_time <= 0:
            on_time += 1

    # compares value vs threshold and print necessary output
    if on_time < threshold:
        print "YES"
    else:
        print "NO"


t = int(raw_input().strip())
for a0 in xrange(t):
    n,threshold = raw_input().strip().split(' ')
    n,threshold = [int(n),int(threshold)]
    arrivals = map(int,raw_input().strip().split(' '))
    is_cancelled(arrivals, threshold)


