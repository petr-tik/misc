#! usr/bin/env python 

# https://www.hackerrank.com/challenges/find-digits

import random

def find_divisors(number):
    # given a number in string form, return the int of its divisors
    number_as_int = int(number)
    divisors = 0
    for digit in number:
        if digit == '1':
            divisors += 1
        elif digit == '0':
            pass
        elif number_as_int % int(digit) == 0:
            divisors += 1
        else:
            pass

    return divisors


T = int(raw_input())

for _ in xrange(T):
    N = str(random.randint(1,100))
    print "{} has {} divisors".format(N, find_divisors(N))