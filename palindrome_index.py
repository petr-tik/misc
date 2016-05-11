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

def word_to_dict(s):
    "takes a string and returns a dict with chars as keys, positions as values"
    res = {}
    for idx, char in enumerate(s):
        if not res.has_key(char):
            res[char] = [idx]
        else:
            res[char].append(idx)

    return res

print is_palindrome('aaa')

def solve(s):
# brute force solution times out, but narrowing the search space doesn't
    if is_palindrome(s):
        print "-1"
# turn the string into a dict with chars as keys 
# and values of indices in the original string
# you don't want to remove a char which appears an even number of times
# so make a candidate space of chars, which appear odd number of times 
# it's enough of an improvement - HackerRank solved
    else:
        word_dict = word_to_dict(s)
        candidates = []
        for key in word_dict:
            if len(word_dict[key]) % 2 != 0:
                candidates.extend(word_dict[key])
        for idx in candidates:
            cand_word = ''.join([s[0:idx], s[idx+1::]])
            if is_palindrome(cand_word):
                print idx
                break


## HackerRank IO boilerplate
N = int(raw_input())
for _ in xrange(N):
    solve(raw_input())

