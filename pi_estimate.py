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
    """
    Area of the square = 1 
    area of the 1/4 square = pi*r^2/4
    when we generate a random pair of coordinates, 
    the probability of hitting the inside of the 1/4 circle is
    P(inside) = pi*r^2/4, where r = 1
    P(inside) = pi/4
    
    to estimate, pi count the number of times they land on the inside, 
    divide it by the number of points and multiply by 4
    
    return 4*(inside/float(N))
    """
    inside = 0
    for _ in xrange(N):
        x, y = xy_gen()
        if sqrt(x**2 + y**2) <= 1.0:
            inside += 1
    return 4*(inside/float(N))

N = int(raw_input("How many experiments do you want to try?\n"))
print solve(N)
