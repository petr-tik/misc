#! usr/bin/env python

# https://www.hackerrank.com/challenges/cut-the-sticks

"""
Input Format 
The first line contains a single integer NN. 
The next line contains NN integers: a0, a1,...aN-1 separated by space, where ai represents the length of ith stick.

Output Format 
For each operation, print the number of sticks that are cut, on separate lines.

"""


def cutting(sticks):
    # given a list of stick lengths print out how many sticks were cut
    lengths = []
    lengths.append(len(sticks))
    while sticks: 
        cut_measure = min(sticks)
        print "new minimum: {}".format(cut_measure)
        sticks = [x-cut_measure for x in sticks if x > cut_measure]
        if sticks:
            lengths.append(len(sticks))
    return lengths        


y = cutting([5,4,5,2,3])
for x in y:
    print x


