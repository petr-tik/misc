#! usr/bin/env python

# https://www.hackerrank.com/challenges/alternating-characters


def s_to_char_loc(s):
    # given a string, return a dict with letters as keys and indices in the string as values
    res = {}
    for idx, char in enumerate(s):
        if not res.has_key(char):
            res[char] = [idx]
        else:
            res[char].append(idx)

    return res


def is_alternate(s):
    # given a string return true if it has alternate chars, otherwise false
    letter_dict = s_to_char_loc(s)
    for key in letter_dict:
        pass

def solve(s):
    letter_dict = s_to_char_loc(s)
    deletions = 0
    if len(letter_dict) == 1:
        deletions = len(s) - 1


    return deletions    


print solve("AAAAAA")


