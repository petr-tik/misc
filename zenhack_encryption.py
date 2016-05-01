#!/usr/bin/env python

import string

# https://www.hackerrank.com/contests/zenhacks/challenges/decrypt-1

def caesar_encrypt(input_string, shift):
    alph = string.lowercase
    res = []
    for char in input_string:
        new_idx = (alph.find(char) + shift) % 26
        res.append(alph[new_idx])
    return "".join(res)


def find_diff(string1, string2):
    # given 2 strings of equal length output the int for different chars
    res = 0
    for idx in xrange(len(string1)):
        if string1[idx] != string2[idx]:
            res += 1
    return res


def solve():
    P,E_dash = raw_input().strip().split(' ')
    P,E_dash = [str(P),str(E_dash)]
    min_mismatch = -1
    for shift in xrange(0, 26):
        E = caesar_encrypt(P, shift)
        diff = find_diff(E, E_dash)
        if min_mismatch == -1 or diff < min_mismatch:
            min_mismatch = diff
    return min_mismatch
    

print caesar_encrypt("abc", 1)
print find_diff('rryyzz', 'xxyyzz')
print solve()