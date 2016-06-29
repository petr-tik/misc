#! /usr/bin/env python 

# estimate pi from N random (x,y) coordinates

import random as rnd
from math import sqrt

def xy_gen():
    x, y = rnd.random(), rnd.random()
    return x, y

def solve(N):
    """Given a number N, run N,generators of x,y coordinates, 
    plot them on the graph and and count how many are inside the circle"""
    inside = 0
    for _ in xrange(N):
        x, y = xy_gen()
        if sqrt(x**2 + y**2) <= 1.0:
            inside += 1

    return 4*(inside/float(N))


print solve(50)
