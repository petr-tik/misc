#! usr/bin/env python

# take 2 words and check if they are anagrams
import string
import random


def make_words():
    # makes two random words
    alphabet = string.lowercase
    word1 = ''.join([alphabet[random.randint(0,25)] for x in xrange(random.randint(1,15))])
    word2 = ''.join([alphabet[random.randint(0,25)] for x in xrange(random.randint(1,15))])
    return word1, word2


def is_anagram(first_word, second_word):
    print "Is {} an anagram of {}?".format(first_word, second_word)
    alphabet = string.lowercase
    word1 = {x : 0 for x in alphabet}
    word2 = {x : 0 for x in alphabet}
    for letter in first_word:
        for letter2 in second_word:
            try:
                word1[letter] += 1
                word2[letter2] += 1
            except IndexError:
                return False

    print word1
    print word2

    if word1 != word2:
        return False
    else:
        return True


for x in xrange(5):
    word1, word2 = make_words()
    print is_anagram(word1, word2)
