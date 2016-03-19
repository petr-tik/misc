import sys

# https://www.hackerrank.com/challenges/utopian-tree

N = int(raw_input())

cache = [0 for _ in xrange(N+1)]

def grow(N):
    # given a number of cycles return the height
    # recursion base case
    if cache[N] != 0:
        return cache[N]

    if N == 0:
        cache[N] = 1
        return 1
    
    else:
        if N % 2 == 1:
            cache[N] = 2*grow(N-1)
        else:
            cache[N] = grow(N-1) + 1
    
    
    return cache[N]


print grow(N)

