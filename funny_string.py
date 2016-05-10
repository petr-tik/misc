#! usr/bin/env python

import string

# https://www.hackerrank.com/challenges/funny-string

def substract_letters(letter1, letter2):
    alph = string.lowercase
    idx1 = alph.index(letter1)
    idx2 = alph.index(letter2)
    return abs(idx1 - idx2)


def is_funny(s):
    # given a string 
    reverse = s[::-1]
    length = len(s)
    for idx in xrange(1, length):
        if substract_letters(s[idx], s[idx - 1]) != substract_letters(reverse[idx], reverse[idx - 1]):
            return False
            break
    return True


N = int(raw_input())
for _ in xrange(N):
    s = raw_input()
    if is_funny(s): 
        print "Funny"
    else:
        print "Not Funny"
