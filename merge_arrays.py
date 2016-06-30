#! /usr/bin/env python 

# Given 2 sorted arrays of length x and y, where x = z + y
# return a merged array

# e.g.
# a = [1, 2, 2, 4, 5, 6, 8, _, _, _]
# b = [5, 8, 9]

# z = merge_arrays_as_queues(a, b)
# z = a = [1, 2, 2, 4, 5, 5, 6, 8, 8, 9]

from collections import deque

a = [1, 2, 2, 4, 5, 6, 8, None, None, None]
b = [5, 8, 9]


def solve(array1, array2):
    """Given 2 sorted arrays of possibly different length, return a merged array"""
    q_a = deque(array1)
    q_b = deque(array2)
    res = [-1 for _ in xrange(len(array1)+len(array2))]
    for idx in xrange(0, len(res)):
        print q_a, q_b
        print res
        if (not q_a) or (q_b[0] < q_a[0]):
            res[idx] = q_b.popleft()
        elif (not q_b) or (q_a[0] < q_b[0]):
            res[idx] = q_a.popleft()
        else:
            res[idx] = q_b.popleft()

    return res


def solve_inplace(array1, array2):
    # append all b values to end of a and then sort
    pass


print solve([1,2,3, 4], [1, 5, 9])

