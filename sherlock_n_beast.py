#! usr/bin/env/ python

from itertools import combinations_with_replacement, combinations

# https://www.hackerrank.com/challenges/sherlock-and-array


"""
need to generate numbers from threes of 5's or fives of 3's 



"""


def can_gen_decent(num_digits):
    rem_from_three = num_digits % 3
    if num_of_digits % 5 == 0 or num_of_digits % 3 == 0 or rem_from_three % 5 == 0: 
        print "we can make a decent number with {} digits".format(num_digits)
    else:
        print "No we cannnot make a decent number with {} digits".format(num_digits)



def generate_decent(num_digits):
    candidates = list(combinations_with_replacement(['3','5'], num_digits))
    decent = []
    for cand in candidates:
        if cand.count('3') % 5 == 0 and cand.count('5') % 3 == 0:
            decent.append(cand)
    print "These are the options", decent
    return decent # a list of candidate tuples in string form


def tup_to_number(tup):
    # takes a tuple of chars 
    # returns an integer made from the chars in tuple
    if not tup:
        return -1
    else:
        res = ''
        for dig in tup:
            res += dig
        return int(res)

def solve():
    for i in xrange(21):
        print i
        x = generate_decent(i)
        if len(x) >= 1:
            res = tup_to_number(x[-1])
            print res

#solve()

def check():
    for i in xrange(21):
        can_gen_decent(i)

check()
