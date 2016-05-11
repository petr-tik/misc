#! /usr/bin/env python

# https://www.hackerrank.com/challenges/palindrome-index

def is_palindrome(s):
    length = len(s)
    if len(s) == 1:
        return True
    if len(s) % 2 == 0:
        halfway = length/2
    else:
        halfway = (length - 1)/2
    for idx in xrange(0, halfway):
        if s[idx] != s[-1 - idx]:
            return False
            break
        else:
            pass
    return True


def solve(s):
    if is_palindrome(s):
        print "-1"
    for idx, char in enumerate(s):
        if is_palindrome(''.join([s[0:idx], s[idx+1::]])):
            print idx
            break

