#! /usr/bin/env python

# https://www.hackerrank.com/challenges/bear-and-steady-gene

# ideas from here
# http://articles.leetcode.com/finding-minimum-window-in-s-which/
# http://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/

the logic is:
look at the BigString and find out how many 


def is_steady(char_dict, length):      
    # takes a dict of chars from string and returns True if already steady        
    if any(len(char_dict[key]) != length/4 for key in char_dict):     
        return False      
    return True

def string_to_dict(string, length):
    substring_length = 0
    char_dict = {'A': [], 'G': [], 'C': [], 'T':[]}
    to_find = {}
    for idx, char in enumerate(string):
        char_dict[char].append(idx)
    
    for key in char_dict:
        difference = len(char_dict[key]) - length/4
        if difference > 0:
            to_find[key] = difference
            substring_length += difference

    return char_dict, to_find, length

    

def solve(string, length):
    # given a string, start looking for relevant substrings, 
    # as soon as you find one, output its length
    char_dict, to_find, substring_length = string_to_dict(string, length)
    if is_steady(char_dict):
        return 0
    while substring_length < length:
        for start_pos in xrange(0, length - substring_length + 1):
            test_string = string[start_pos:start_pos + substring_length]
            if all(test_string.count(x) == to_find[x] for x in to_find):
                return substring_length
                break
        substring_length += 1
    return length
                
print string_to_dict('TGATGCCGTCCCCTCAACTTGAGTGCTCCTAATGCGTTGC', 40)

# HackerRank boilerplate
"""length = int(raw_input())
string = raw_input()
print solve(string, length)
"""
