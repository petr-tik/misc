#! /usr/bin/env/ python

import os
from itertools import permutations

""" 
Original Problem:

Given a collection of letters, scrabble board and a reference dictionary, 
return the best-scoring word on a scrabble board.

Harder Problem:
Given a partially filled-in scrabble board, return the best-scoring word
"""

"""
Solution idea:
2 problems:
   * Given letters, generate words in dictionary and sort them by value
   * Find which word is placed best to give the best result
First generate possible words from given letters
Sort words by their letter-score
Try all possible placements on an empty scrabble board, keep max_value, return the best word. 


"""     

with open('/../../usr/share/dict/words') as f:
    DICTIONARY = f.read().splitlines()


def generate_legit_words(letters, ref_dict):
    """ 
    Given an array of chars for letters and a reference dictionary, 
    return a list (could be empty) of words that can be made of these letters 

    Brute force: generate all permutations of letters, check which ones are in the
    dictionary

    Optimal: 

    """
    words = []
    for length in xrange(2,len(letters)):
        words.extend((''.join(x) for x in permutations(letters, length)))

    return words


print generate_legit_words(['y', 'a', 'd'], DICTIONARY)


##class Scrabble(object):
##    def __init__(self):
        
        


