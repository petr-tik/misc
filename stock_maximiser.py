#! usr/bin/env python

# https://www.hackerrank.com/challenges/stockmax

import random

"""
T = int(raw_input())
for _ in xrange(T):
    number = int(raw_input())
    datapoints = [int(x) for x in raw_input().split()]
"""

def max_to_end(L):
    """ Given a list of ints 
    ints =         [91,  76,  63,  125, 148, 40,  43,  186, 108, 123] 
    max_from_pos = [186, 186, 186, 186, 186, 186, 186, 186, 123, 123]

    returns a list of values, where max_from_pos[i] is the greatest int from index i to the end of the array
    """
    temp_max = L[-1]
    output_list = []
    output_list.append(temp_max) 
    # appended from the end, so needs reversing
    for idx in xrange(len(L) - 2, -1, -1):
        if L[idx] > temp_max:
            temp_max = L[idx]
        output_list.append(temp_max)

    return output_list[::-1] # reversed as per comment above


def maximise_profit(datapoints, max_values):
    """ Givent the datapoints and max_values from index i to end, return balance
    The key is: 
         if price available now isn't the maximum between now and end - buy 1 share
         if price available now is the maximum - sell all. 

    You NEVER sell just 1 share, if you sell, sell them all
    """
    print "Starting with {}".format(datapoints)
    balance = 0
    shares_bought = 0
    for idx, price in enumerate(datapoints):
        if price >= max_values[idx]:
            balance += shares_bought*price
            print "Selling {} shares for {}".format(shares_bought, price)
            shares_bought = 0
        else:
            balance -= price
            shares_bought += 1
            print "Buying one share for {}".format(price)

        print "Given the array {} the balance is {}".format(datapoints[:idx+1], balance)

    print balance


for x in xrange(5):
    datapoints = [random.randint(1,200) for x in xrange(10)]
    print datapoints, max_to_end(datapoints)
    maximise_profit(datapoints, max_to_end(datapoints))
