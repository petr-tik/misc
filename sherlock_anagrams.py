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
    # consider all substring lengths between 1 (one char) to (n - 1)
    answer = 0
    for subarray_lengths in xrange(1, n): # will only consider non-empty strings 
        length = n - subarray_lengths 
        under_investigation = []
        # given the length, make a range of starting points, 
        # so you can make strings of that length from each start position
        for start_pos in xrange(0, n - length + 1):
            word = phrase[start_pos:start_pos+length]
            dict_from_word = make_dict(word)
            if answer == 0 and dict_from_word in under_investigation:
                answer += 2
            elif dict_from_word in under_investigation:
                answer += 1
            else:
                under_investigation.append(dict_from_word)
    print answer 


count_anagrams("abba")
count_anagrams("ifailuhkqq")
count_anagrams("hucpoltgty")
count_anagrams("ovarjsnrbf")
count_anagrams("pvmupwjjjf")
count_anagrams("iwwhrlkpek")

"""
T = int(raw_input()) # number of test cases
for x in xrange(T):
    count_anagrams(raw_input())

"""



