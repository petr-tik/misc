#! /usr/bin/env python

# https://www.hackerrank.com/challenges/bear-and-steady-gene

def analyse(string, length):
    substring_length = 0
    char_dict = {'A': [], 'G': [], 'C': [], 'T':[]}
    too_many = {}
    for idx, char in enumerate(string):
        char_dict[char].append(idx)
    
    for key in char_dict:
        difference = len(char_dict[key]) - length/4
        if difference > 0:
            too_many[key] = difference
            substring_length += difference


    return char_dict, too_many, substring_length



def solve(string, length):
    # given a string, start looking for relevant substrings, 
    # as soon as you find one, output its length
    char_dict, too_many, substring_length = analyse(string, length)
    while substring_length < length:
        for start_pos in xrange(0, length - substring_length + 1):
            test_string = string[start_pos:start_pos + substring_length]
            if all(test_string.count(x) == too_many[x] for x in too_many):
                return substring_length
                break
        substring_length += 1
    return length
                
print solve('TGATGCCGTCCCCTCAACTTGAGTGCTCCTAATGCGTTGC', 40)


# HackerRank boilerplate
"""length = int(raw_input())
string = raw_input()
print solve(string, length)
"""
