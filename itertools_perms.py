#! usr/bin/env python

# https://www.hackerrank.com/challenges/itertools-permutations

from itertools import permutations

string, dimension = raw_input().split()
dim = int(dimension)

for x in sorted(permutations(string, dim)):
    print "".join(x)