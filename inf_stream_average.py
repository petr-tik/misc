#! /usr/bin/env python3

""" Calcuate the average of an infinite stream of numbers 
fb interview puzzle
"""

import random as rnd


def gen_number(l_limit, u_limit):
    return rnd.randint(l_limit, u_limit)


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


def gen_inf_stream():
    """ Infinite generator """
    low = 0
    high = 120
    yield(rnd.randint(low, high))


def gen_mean_from_infinite_stream(gen_inf_stream):
    """ Input: 
              Generator that yields the next value
        Yields:
              average so far
    """


for next_avg in gen_mean_so_far(10, 15):
    print(next_avg)
