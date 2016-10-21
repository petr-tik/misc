#! /usr/bin/env/ python

import os
from itertools import permutations, combinations
import string
import random as rnd
import unittest
from functools import reduce

"""
Original Problem:

Given a collection of letters, a scrabble board state (default=empty) and a reference dictionary,
return the best-scoring word on that scrabble board.

Harder Problem:
Given a partially filled-in scrabble board, return the best-scoring word
"""
"""
Solution idea:
2 problems:
   * Given letters, generate words in dictionary and sort them by value
   * Find which word is placed best to give the best result
First generate possible words from given letters - 3 methods
1. brute force letter permutations
2. dfs on the dictionary given all possible stacks of letters
3. Make a dictionary length : word : score structure, where words of length are sorted according to score. Given letters make all possible words from letters, sort by length and travers each subdict for the best scoring word


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


def my_and(x, y):
    return x & y

ROW_LENGTH = reduce(my_and, [len(row) for row in EMPTY_BOARD])


def generate_letters(num):
    """ Given an int, return a list of num random letters """
    alph = string.lowercase
    return [rnd.choice(alph) for _ in xrange(num)]


# brute force words generation

def generate_words_brute(letters, ref_dict=DICTIONARY):
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


# 2nd idea for word generation - implement dfs for words in dictionary
# with given letters (like a stack in dfs)

def dict_from_seq(seq):
    """ Given a sequence (array or string) of alphabetic chars,
    return a hashmap/dict of chars and counts
    """
    hashmap = {}
    for item in seq:
        if item not in hashmap:
            hashmap[item] = 0
        hashmap[item] += 1
    return hashmap


def dfs_in_dict(letters, ref_dict, words_so_far=set()):
    """ Given letters, a dictionary and (optionally) an array of words,
    search for words you can make from letters.
    Use Depth-First search-like idea:
    First, find all words with 1st letter, then in the subset words with the 2nd
    letters, after that check if >3 letters (2 old, 1 new)
    make a word in the dictionary.
    If so, add it to the words_so_far array,
    if no words contain the letters,
    drop the last letter you added and try with the next one

    """
    search_space = []
    letters_so_far = []
    for idx, letter in enumerate(letters):
        print words_so_far
        letters_so_far.append(letter)
        if not search_space:
            # start just all words with such first letter
            search_space = [w for w in ref_dict if letter in w]
        else:
            search_space = [w for w in search_space if letter in w]
        words_from_letters = [w for w in search_space if dict_from_seq(
            w) == dict_from_seq(letters_so_far)]
        if idx >= 3 and words_from_letters:
            for word in words_from_letters:
                words_so_far.add(word)
    return words_so_far


def generate_words_dfs(letters, ref_dict=DICTIONARY):
    return dfs_in_dict(letters, ref_dict)


# 3rd idea for word generation - preprocess optimal positions for high-scoring letters given all possible word lengths
# works really well for empty board - you work out the best placement of an x-long
# string and find such words, where letter multiplier cells fall
# on high-worth words.
# Word length means it will land on same strip to collect word multipliers


###
# Scoring - also brute force
# scoring word on given strip of board
# calculating the max score for a word on a board in a state (default=empty)
###

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
    """ Given an array of words and a board state (default = empty)
    return a tuple of word and its score for the highest scoring word
    on such a board layout """
    print words
    max_value = -1
    max_word = ""
    for word in words:
        max_word_score = max_score_on_board(word)
        if max_value == -1 or max_word_score > max_value:
            max_value = max_word_score
            max_word = word

    return max_word, max_value


###
# Testing all of the above
# first separate functions
# then different methods' equivalence
###


class TestScrabble(unittest.TestCase):

    def test_queue_is_72_on_empty(self):
        """ Testing that the word queue scores 72 on an empty board """
        self.assertEqual(72, max_score_on_board("queue"))

    def test_dfs_and_brute_word_gen(self):
        """ Testing that brute force and dfs search 
        return the same result for random letters """
        letters = generate_letters(6)
        print letters
        brute_words = generate_words_brute(letters)
        dfs_words = generate_words_dfs(letters)
        self.assertEqual(brute_words, dfs_words)

    def test_dfs_and_brute_amazon(self):
        amazon = ['a', 'm', 'a', 'z', 'o', 'n']
        self.assertEqual(generate_words_dfs(amazon),
                         generate_words_brute(amazon))


if __name__ == '__main__':
    """
    for _ in xrange(5):
        rand_letters = generate_letters(6)
        print rand_letters
        x = find_max_word_and_score(generate_words_brute(rand_letters))
        print x
    """
    unittest.main(verbosity=10)
