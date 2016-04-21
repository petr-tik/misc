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



def count_anagrams(phrase):
    n = len(phrase)
    for subarrays in xrange(2, n):
        length = n - subarrays + 1







