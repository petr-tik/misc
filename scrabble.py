#! /usr/bin/env/ python

import os
from itertools import permutations, combinations
import string
import random as rnd
import unittest
from functools import reduce

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

# Scrabble board consists of 8 arrays,
# 7 which repeat themselves as 2 rows and 2 columns
# 1 (central/middle) repeats as just row and column
# each cell is defined as multiplier (int)
# and category (word or letter multiplier)
# 3w - multiplies the score of the whole word by 3
# 2l - multiplies the score of letter by 2
# Each cell string qualifier is unpacked in the evaluator function

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
    Given an array of chars for letters 
    and a reference dictionary (default = English dictionary from unix),
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


def score_word_on_strip(word, board_strip):
    """
    Given a word and an equal-length strip of board,
    return the number of points
    """
    scores = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1,
              'n': 1, 's': 1, 't': 1, 'r': 1, 'd': 2, 'g': 2,
              'b': 3, 'c': 3, 'm': 3, 'p': 3, 'f': 4, 'h': 4,
              'v': 4, 'w': 4, 'y': 4, 'k': 5, 'j': 8, 'x': 8,
              'q': 10, 'z': 10}
    word_mult = 1
    letters_running_total = 0
    for idx, cell in enumerate(board_strip):
        letter_value = scores[word[idx]]
        if cell[1] == 'w':
            word_mult *= int(cell[0])
            letters_running_total += letter_value
        else:
            letter_mult = int(cell[0])
            letters_running_total += letter_mult * letter_value
    return word_mult * letters_running_total


# print score_word_on_strip(word_score("amazon"), EMPTY_BOARD[0][:5])


def max_score_on_board(word, board_state=EMPTY_BOARD):
    """
    Given a word and a scrabble board state (default: empty),
    return the maximum points this word can score on this board state
    """
    max_score = -1
    word_len = len(word)
    for row in board_state:
        for idx in xrange(ROW_LENGTH - word_len):
            word_value_on_this_strip = score_word_on_strip(
                word, row[idx:idx + word_len])
            max_score = max(word_value_on_this_strip, max_score)

    return max_score


def find_max_word_and_score(words, board_state=EMPTY_BOARD):
    print words
    max_value = -1
    max_word = ""
    for word in words:
        max_word_score = max_score_on_board(word)
        if max_value == -1 or max_word_score > max_value:
            max_value = max_word_score
            max_word = word

    return max_word, max_value


class TestScrabble(unittest.TestCase):

    def test_word_score(self):
        pass
        # self.assertEqual(17, word_score('amazon'))

    def test_word_score2(self):
        pass
        # self.assertEqual(13, word_score('kremlin'))

    def test_word_score3(self):
        pass
        # self.assertEqual(10, word_score('bridge'))

    def test_strip_equals_word_len(self):
        pass

# print generate_legit_words(generate_letters(6), DICTIONARY)


# class Scrabble(object):
# def __init__(self):

if __name__ == '__main__':
    rand_letters = generate_letters(8)
    print rand_letters
    x = find_max_word_and_score(generate_legit_words(rand_letters))
    print x
    # unittest.main(verbosity=10)
