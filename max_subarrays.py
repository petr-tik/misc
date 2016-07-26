#! /usr/bin/env python

# https://www.hackerrank.com/challenges/maxsubarray

def max_cont(arr, res):
    """
    Given an array and a starting value, return the sum of the maximum contiguous array
    Solve dynamically
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
    """ To find the max non-contiguous sum, add up all positive integers """
    non_cont_sum = 0
    for element in arr:
        if element > 0:
            non_cont_sum += element
    return non_cont_sum


def max_subarrays(arr):
    """
    Given an array, return the maximum possible sums of:
        contiguous 
        non-contiguous subarray
    """
    res = 0
    max_cont_sum =  max_cont(arr, res)
    return max_cont_sum, max_non_cont(arr)

# print max_subarrays([2, -1, 2, 3, 4, -5])
print max_cont([-3, -1, -5], -3)
print max_non_cont([-3, -1, -5])
