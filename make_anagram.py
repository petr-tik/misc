#! /usr/bin/env python

import string

# https://www.hackerrank.com/challenges/make-it-anagram

def word_to_dict(s):
    alph = string.lowercase
    res = {char:0 for char in alph}
    for char in s:
        res[char] += 1
    return res

def solve():
    word1 = raw_input()
    word2 = raw_input()
    dict1 = word_to_dict(word1)
    dict2 = word_to_dict(word2)
    res = 0
    for key in dict1:
        number1 = dict1[key]
        number2 = dict2[key]
        if number1 == number2:
            pass
        else:
            res += max(number1, number2) - min(number1, number2)
    return res
