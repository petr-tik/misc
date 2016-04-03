#! usr/bin/env python

# https://www.hackerrank.com/challenges/stockmax

import random

"""
T = int(raw_input())
for _ in xrange(T):
    number = int(raw_input())
    datapoints = [int(x) for x in raw_input().split()]
"""



def maximise_profit(datapoints):
    print "Starting with {}".format(datapoints)
    balance = 0
    shares_bought = 0
    for idx, price in enumerate(datapoints):
        if price >= max(datapoints[idx:]):
            balance += shares_bought*price
            print "Selling {} shares for {}".format(shares_bought, price)
            shares_bought = 0

        else:            
            balance -= price
            shares_bought += 1
            print "Buying one share for {}".format(price)
            

        print "Given the array {} the profit is {}".format(datapoints[:idx+1], balance)

    print balance



for x in xrange(5):
    datapoints = [random.randint(1,200) for x in xrange(10)]
    maximise_profit(datapoints)