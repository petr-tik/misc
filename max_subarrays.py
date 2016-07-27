#! /usr/bin/env python

# https://www.hackerrank.com/challenges/maxsubarray

MAX_INT_VALUE = 1000

""" 
Given an array of ints between -MAX_VALUE < int < MAX_VALUE 
return the sum of maximum contiguous and non-contiguous array
"""

def max_cont(arr, res):
    """
    Given an array and a starting value, return the sum of the maximum contiguous array
    Solve dynamically
    [2, 6, -9]           returns 8
    [-3, -1, -5]         returns -1
    [2, -1, 2, 3, 4, -5] returns 10
    [6, -7, 2, 3, 4, -5] returns 9
    """
    if not arr:
        return res

    new_val = arr.pop(0)
    print arr, new_val, res
    if res + new_val < 0:
        res = max(res, new_val)
        print res
        max_cont(arr, res)


def max_non_cont(arr):
    """ To find the max non-contiguous sum, add up all positive integers 
    if all ints are negative, find and returns the largest
    """

    non_cont_sum = 0
    all_negatives_max = -MAX_INT_VALUE
    for element in arr:
        if element > 0:
            non_cont_sum += element
        else:
            # if all ints are negative, this will hold the maximum value, which we will take
            all_negatives_max = max(element, all_negatives_max)

    if non_cont_sum == 0: 
        return all_negatives_max
    else:
        return non_cont_sum


def solve(arr):
    """
    Given an array, return the maximum possible sums of:
        contiguous 
        non-contiguous subarray
    """
    res = 0
    max_cont_sum =  max_cont(arr, res)
    return max_cont_sum, max_non_cont(arr)

# print solve([2, -1, 2, 3, 4, -5])
print max_cont([-1, -5], -3)
print max_cont([-3, -1, -5], -6)

