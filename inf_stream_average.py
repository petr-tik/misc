#! /usr/bin/env python3

""" Calcuate the average of an infinite stream of numbers 
fb interview puzzle
"""

import random as rnd


def gen_number(l_limit, u_limit):
    yield rnd.randint(0, 50)


for x in xrange(gen_number(5, 10)):
    print x

def calc_mean(mean_so_far, counter, new_val):
    """ Input:
              mean value so far 
              Counter of ints
              a new value
        Output: 
              the new average value
    """
    if counter == 0:
        return new_val
    return (mean_so_far * counter + new_val) / (counter + 1)


def gen_mean_so_far(start, finish):
    """ Input:
              start value
              finish value
        Generates/yields:
              average so far
    """

    mean_so_far = 0
    counter = 0
    for item in range(start, finish):
        mean_so_far = calc_mean(mean_so_far, counter, item)
        yield(mean_so_far)
        counter += 1

for next_avg in gen_mean_so_far(10, 15):
    print(next_avg)
