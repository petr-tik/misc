#! usr/bin/env/ python

from itertools import combinations_with_replacement

# https://www.hackerrank.com/challenges/sherlock-and-array

def generate_decent(num_digits):
    candidates = list(combinations_with_replacement('35', num_digits))
    decent = []
    for cand in candidates:
        if cand.count('3') % 5 == 0 and cand.count('5') % 3 == 0:
            decent.append(cand)

    return decent


def tup_to_number(tup):
    # takes a tuple of chars 
    # returns an integer made from the chars in tuple
    if not tup:
        return 0
    else:
        res = ''
        for dig in tup:
            res += dig
        return int(res)

def solve():
    for i in xrange(21):
        x = generate_decent(i)
        if len(x) >= 1:
            res = tup_to_number(x[-1])
            print res


solve()