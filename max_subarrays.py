#! /usr/bin/env python

# https://www.hackerrank.com/challenges/maxsubarray

import unittest

MAX_INT_VALUE = 1000

""" 
Given an array of ints between -MAX_VALUE < int < MAX_VALUE 
return the sum of maximum contiguous and non-contiguous subarrays
"""

def max_cont(arr, res):
    """
    Given an array and a starting value, return the sum of the maximum contiguous array
    Solve dynamically
    [2, 6, -9]           returns 8
    [-3, -1, -5]         returns -1
    [2, -1, 2, 3, 4, -5] returns 10
    [6, -7, 2, 3, 4, -5] returns 9
    [6, -7, 2, 3, -5]    returns 6

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


class TestSolve(unittest.TestCase):
    def setUp(self):
        self.arr1 = [2, 6, -9]
        self.arr2 = [-3, -1, -5]
        self.arr3 = [2, -1, 2, 3, 4, -5]
        self.arr4 = [6, -7, 2, 3, 4, -5]
        self.arr5 = [6, -7, 2, 3, -5]


    def test_max_cont1(self):
        self.assertEqual(8, max_cont(self.arr1, 0))

    def test_max_cont2(self):
        self.assertEqual(-1, max_cont(self.arr2, 0))

    def test_max_cont3(self):
        self.assertEqual(10, max_cont(self.arr3, 0))
                         
    def test_max_cont4(self):
        self.assertEqual(9, max_cont(self.arr4, 0))

    def test_max_cont5(self):
        self.assertEqual(6, max_cont(self.arr5, 0))


if __name__ == '__main__':
    print max_cont([-1, -5], -3)
    print max_cont([-3, -1, -5], -6)
    
    # unittest.main()
    
