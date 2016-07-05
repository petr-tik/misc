#! /usr/bin/env python

# https://www.hackerrank.com/challenges/bear-and-steady-gene

# ideas from here
# http://articles.leetcode.com/finding-minimum-window-in-s-which/
# http://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/

# the logic is:
# look at the BigString and find out how many chars are missing. Make a hashmap with count for its missing character.
# go through the string again with begin and start pointers. When you find all the missing chars, mark the end pointer to the last char and record the overall length of the window 
# try to move the start pointer as far left as possible. Go through the rest of BigString looking to move the start pointer as far right as possible. 


def analyse(string, length):
    """Takes a string and its length 
    and returns 
        the dictionary of characters
        the dictionary of chars to find 
        absolute minimum length of a substring to be replaced
    """

    abs_min_length = 0
    char_dict = {'A': 0, 'G': 0, 'C': 0, 'T':0}
    
    # makes a counter of times each character appears
    for idx, char in enumerate(string):
        char_dict[char] += 1
    
    # makes a to_find dictionary with the counter 
    # for how many times we need each char in a substring and its min length
    need_to_find = {}
    for key in char_dict:
        difference = char_dict[key] - length/4
        if difference > 0:
            need_to_find[key] = difference
            # absolute minimal length of substring
            abs_min_length += difference
        else:
            need_to_find[key] = 0

    return char_dict, need_to_find, abs_min_length

    

def solve(string, length):
    # given a string, start looking for relevant substrings, 
    # as soon as you find one, output its length
    char_dict, need_to_find, abs_min_length = analyse(string, length)
    has_found = {'A': 0, 'G': 0, 'C': 0, 'T':0}
    min_substring_length = length + 1
    counter = 0
    start_pointer = 0
    for end_pointer in xrange(length):
        end_char = string[end_pointer]
        if need_to_find[end_char] == 0:
            continue # if we don't need it - keep advancing the end pointer
        # otherwise, do as below
        has_found[end_char] += 1
        
        if has_found[end_char] <= need_to_find[end_char]:
            counter += 1 
        if counter == abs_min_length: 
            # advance begin index as far right as possible,
            # stop when advancing breaks window constraint.
            while need_to_find[string[start_pointer]] == 0 or has_found[string[start_pointer]] > need_to_find[string[start_pointer]]:
                slide_char = string[start_pointer]
                if (has_found[slide_char] > need_to_find[slide_char]):
                    has_found[slide_char] -= 1
                start_pointer += 1
          
            window = end_pointer - start_pointer + 1
            if window < min_substring_length:
                min_substring_length = window

    return min_substring_length 


                
print solve('TGATGCCGTCCCCTCAACTTGAGTGCTCCTAATGCGTTGC', 40)
print solve('TTTT', 4)
print solve('GAAATAAA', 8)

# HackerRank boilerplate
# length = int(raw_input())
# string = raw_input()
# print solve(string, length)

