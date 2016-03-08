#! usr/bin/env/ python
# https://www.hackerrank.com/challenges/pangrams
import string

alphabet = string.ascii_lowercase

def is_pangram(s):
    # given a string, return True if it's a pangram, otherwise, return False
    # make a dict with letters as keys, if char found in string increment the value. 
    # At the end of string, if dict has 0 value anywhere, it's not a pangram
    # remove all spacing 
    s = s.replace(" ", "")
    alph_dict = {}
    for char in alphabet:
        alph_dict[char] = 0

    # step through the string (lowercased)
    for char in s.lower():
        # increment the value on the particular key
        alph_dict[char] += 1

    # if there is at least one 0 in list of values - at least one letter never appeared in the string    
    if 0 in alph_dict.values():
        print "not pangram"
    else:
        print "pangram"
    

is_pangram("hello how are you you beautiful bastard who lives in china before america takes over")
is_pangram("The quick brown fox jumps over the lazy dog")
is_pangram("We promptly judged antique ivory buckles for the next prize")
is_pangram("We promptly judged antique ivory buckles for the prize")
