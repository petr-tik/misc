#! usr/bin/env python

# https://www.hackerrank.com/contests/zenhacks/challenges/candy-shop

import sys


def solve():
    """ Requests input, creates a cache array and returns the answer,
    using the method defined internally """
    value = int(raw_input().strip())
    coin_values = [1, 2, 5, 10, 20, 50, 100]
    cache = [[-1 for _ in coin_values] for _ in xrange(value + 1)]

    def calc_ways_to_make_number_from_coins(NUMBER, start_coin=0):
        """ Given a value and a start coin value index (default = 0)
        return the number of ways to make value
        by combining an infinite number of coins of given values
        """
        # check if the value has been calculated
        if cache[NUMBER][start_coin] != -1:
            return cache[NUMBER][start_coin]

        res = 0

        if NUMBER == 0:
            res = 1

        else:
            for i in xrange(start_coin, len(coin_values)):
                if coin_values[i] <= NUMBER:
                    res += calc_ways_to_make_number_from_coins(
                        NUMBER - coin_values[i], i)
                else:
                    break

        cache[NUMBER][start_coin] = res
        return res

    return calc_ways_to_make_number_from_coins(value)

print solve()
