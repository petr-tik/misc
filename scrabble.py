#! /usr/bin/env/ python

import os
from itertools import permutations, combinations
import string
import random as rnd
import unittest

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
    DICTIONARY = [x.lower() for x in f.read().splitlines()]
    # print DICTIONARY

EMPTY_BOARD = [['3w', '1l', '1l', '2l', '1l', '1l', '1l',
                '3w', '1l', '1l', '1l', '2l', '1l', '1l', '3w'],
               ['1l', '2w', '1l', '1l', '1l', '3l', '1l',
                '1l', '1l', '3l', '1l', '1l', '1l', '2w', '1l'],
               ['1l', '1l', '2w', '1l', '1l', '1l', '2l',
                '1l', '2l', '1l', '1l', '1l', '2w', '1l', '1l'],
               ['2l', '1l', '1l', '2w', '1l', '1l', '1l',
                '2l', '1l', '1l', '1l', '2w', '1l', '1l', '2l'],
               ['1l', '1l', '1l', '1l', '2w', '1l', '1l',
                '1l', '1l', '1l', '2w', '1l', '1l', '1l', '1l'],
               ['1l', '3l', '1l', '1l', '1l', '3l', '1l',
                '1l', '1l', '3l', '1l', '1l', '1l', '3l', '1l'],
               ['1l', '1l', '2l', '1l', '1l', '1l', '2l',
                '1l', '2l', '1l', '1l', '1l', '2l', '1l', '1l'],
               ['3w', '1l', '1l', '2l', '1l', '1l', '1l',
                '2w', '1l', '1l', '1l', '2l', '1l', '1l', '3w']]


def generate_letters(num):
    """ Given an int, return a list of num random letters """
    alph = string.lowercase
    return [rnd.choice(alph) for _ in xrange(num)]


def word_score(word):
    """ Given a word, return a list of tuples in form (letter, score) """
    scores = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1,
              'n': 1, 's': 1, 't': 1, 'r': 1, 'd': 2, 'g': 2,
              'b': 3, 'c': 3, 'm': 3, 'p': 3, 'f': 4, 'h': 4,
              'v': 4, 'w': 4, 'y': 4, 'k': 5, 'j': 8, 'x': 8,
              'q': 10, 'z': 10}
    res = []
    for letter in word:
        res.append((letter, scores[letter]))
    return res


def generate_legit_words(letters, ref_dict=DICTIONARY):
    """
    Given an array of chars for letters and a reference dictionary,
    return a list (could be empty) of words that can be made of these letters

    Brute force: generate all permutations of letters, check which ones are in the
    dictionary

    Optimal:

    """
    words = []
    for length in xrange(2, len(letters) + 1):
        cand_words = [''.join(x) for x in permutations(letters, length)]
        for word in cand_words:
            # if chars repeat, permutations will produce multiple examples of
            # word
            if word in ref_dict and word not in words:
                words.append(word)
    return words


def score_words(legit_words):
    """
    Given a list of legit words (in the dict),
    return a list of tuples of the form (word_string, word_score)
    """
    words_with_scores = []
    for word in legit_words:
        words_with_scores.append((word, word_score(word)))

    return words_with_scores


x = generate_legit_words(['q', 'u', 'e', 'e', 'u'])
print score_words(x)


# print generate_legit_words(generate_letters(6), DICTIONARY)


# class Scrabble(object):
# def __init__(self):


class TestScrabble(unittest.TestCase):

    def test_word_score(self):
        self.assertEqual(17, word_score('amazon'))

    def test_word_score2(self):
        self.assertEqual(13, word_score('kremlin'))

    def test_word_score3(self):
        self.assertEqual(10, word_score('bridge'))

if __name__ == '__main__':
    unittest.main(verbosity=10)
