#! /usr/bin/env python 

# https://www.hackerrank.com/challenges/taum-and-bday

def solve(num_black, num_white, price_black, price_white, price_sub):
    if price_black + price_sub < price_white:
        return num_black*price_black + num_white*(price_black + price_sub)
    elif price_white + price_sub < price_black:
        return num_white*price_white + num_black*(price_white + price_sub)
    else:
        return num_black*price_black + num_white*price_white


# hackerrank boilerplate
t = int(raw_input().strip())
for a0 in xrange(t):
    b,w = raw_input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    print solve(b,w,x,y,z)
