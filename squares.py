#! usr/bin/env python 

import math

# https://www.hackerrank.com/challenges/sherlock-and-squares

def find_squares(lower, upper):
    # given inclusive lower and upper bounds, 
    # return the number of square ints between them
    num_of_squares = 0
    for number in xrange(lower, upper + 1):
        square = math.sqrt(number)
        print square
        if square.is_integer():
            num_of_squares += 1
            if (square + 1)**2 > upper + 1:
                print "the next square is too big"
                break
        else:
            pass

    return num_of_squares


T = int(raw_input())

for _ in xrange(T):
    lower, upper = map(int,raw_input().split())
    print find_squares(lower, upper)


