#! /usr/bin/env python

""" Calcuate the average of an infinite stream of numbers """

import random as rnd


def gen_number(l_limit, u_limit):
    yield rnd.randint(0, 50)


for x in xrange(gen_number(5, 10)):
    print x
