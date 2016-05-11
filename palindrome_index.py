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
    if is_palindrome(s):
        print "-1"
    
    word_dict = word_to_dict(s)

    candidates = []
    for key in word_dict:
        if len(word_dict[key]) % 2 != 1:
            candidates.extend(word_dict[key])

    for idx in candidates:
        if is_palindrome(''.join([s[0:idx], s[idx+1::]])):
            print idx
            break

