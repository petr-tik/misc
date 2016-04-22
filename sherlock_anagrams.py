#! usr/bin/env/ python

# https://www.hackerrank.com/challenges/sherlock-and-anagrams

def make_dict(word):
    "takes a string and returns a dict with character as key, count as value"
    letters_in_words = {}
    for char in word:
        if char in letters_in_words:
            letters_in_words[char] += 1
        else:
            letters_in_words[char] = 1

    return letters_in_words


def are_anagrams(string1, string2):
    "takes 2 (sub)strings and checks if they are anagrams using the make_dict helper"
    if make_dict(string1) == make_dict(string2):
        return True
    else:
        return False 


def count_anagrams(phrase):
    "iterate over the big string and check pairs of substrings of same length"
    n = len(phrase)
    for subarrays in xrange(2, n + 1):
        length = n - subarrays + 1
        for x in xrange(0, n - length + 1):
            print phrase[x:x+length]

count_anagrams("abcdefgh")







