#! usr/bin/env python

# https://www.hackerrank.com/challenges/candies

import random

"""
N = int(raw_input())

candies = [1 for _ in xrange(N)]


ratings = []
for _ in xrange(N):
    ratings.append(int(raw_input()))
"""
# print len(candies), candies

candies = [1 for _ in xrange(10)]

ratings = [random.randint(1,20) for _ in xrange(10)]
print ratings

ratings_spec = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]


def candy_calc(ratings):
    for idx in xrange(1, len(ratings)):
        cur = ratings[idx]
        prev = ratings[idx - 1]
        
        if cur > prev:
            candies[idx] = candies[idx - 1] + 1

        elif prev > cur:
            # if prev
            

        print candies

    return sum(candies)

print "We need to buy {} candies".format(candy_calc(ratings))
print ratings_spec
print "We need to buy {} candies".format(candy_calc(ratings_spec))
