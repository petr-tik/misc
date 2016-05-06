#! usr/bin/env/ python

from itertools import combinations

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


def are_anagrams(tup):
    "takes a tuple of dicts and checks if they are anagrams"
    dict1 = tup[0]
    dict2 = tup[1]
    if cmp(dict1, dict2) == 0:
        return True
    else:
        return False 


def count_anagrams(phrase):
    "iterate over the big string and check pairs of substrings of same length"
    n = len(phrase)
    # consider all substring lengths between 1 (one char) to (n - 1)
    answer = 0
    for subarray_length in xrange(n - 1, 0, -1): # will only consider non-empty strings 
        under_investigation = []
        # given the length, make a range of starting points, 
        # so you can make strings of that length from each start position
        for start_pos in xrange(0, n - subarray_length + 1):
            # make a new word of new length from star_pos 
            word = phrase[start_pos:start_pos+subarray_length]
            # make a dict from that word
            dict_from_word = make_dict(word)
            under_investigation.append(dict_from_word)
        
        # make unordered pairs (combinations) of all dicts of the same length strings
        pairs_of_equal_length_dicts = list(combinations(under_investigation, 2))
        # the number of tuples that return true on make_dict is added to final answer
        num_of_anagrams = len(filter(are_anagrams, pairs_of_equal_length_dicts))
        answer += num_of_anagrams
    print answer 


count_anagrams("abba")
print "should be", 3
count_anagrams("ifailuhkqq")
print "should be", 2
count_anagrams("hucpoltgty")
print "should be", 2
count_anagrams("ovarjsnrbf")
print "should be", 6
count_anagrams("pvmupwjjjf")
print "should be", 3
count_anagrams("iwwhrlkpek")

"""
T = int(raw_input()) # number of test cases
for x in xrange(T):
    count_anagrams(raw_input())

"""



