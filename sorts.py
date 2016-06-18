#! /usr/bin/env python

## different sorting algos
import unittest
import random

def binary_sort(arr):
    pass

def bubble_sort(arr):
    length = len(arr)
    for cur_idx in xrange(0, length):
        for next_idx in xrange(0, length - 1):
            if arr[next_idx] > arr[next_idx+1]:
                temp = arr[next_idx]
                arr[next_idx] = arr[next_idx+1]
                arr[next_idx+1] = temp
                #print "Swapped {} for {}".format(arr[next_idx + 1], arr[next_idx])
                #print arr
    return arr

def insertion_sort(arr):
    length = len(arr)

    for idx_in_unsorted in xrange(1, length):
        moving_item = arr[idx_in_unsorted]
        idx_in_sorted = idx_in_unsorted - 1
        while idx_in_sorted >= 0 and arr[idx_in_sorted] > moving_item:
            arr[idx_in_sorted + 1] = arr[idx_in_sorted]
            idx_in_sorted -= 1
        idx_in_sorted += 1
        arr[idx_in_sorted] = moving_item

    return arr



class TestSorts(unittest.TestCase):
    """docstring for ClassName"""
    def setUp(self):
        self.length = 15
        self.list1 = [random.randint(0,25) for _ in xrange(self.length)]

    def test_bubble_sort(self):
        list1 = bubble_sort(self.list1)
        for idx in xrange(1, self.length):
            self.assertTrue(list1[idx - 1] <= list1[idx])

    def test_insertion_sort(self):
        list1 = insertion_sort(self.list1)
        for idx in xrange(1, self.length):
            self.assertTrue(list1[idx - 1] <= list1[idx])

    def test_sorts_equal(self):
        self.assertEqual(bubble_sort(self.list1), insertion_sort(self.list1))


if __name__ == '__main__':
    unittest.main(verbosity=10)