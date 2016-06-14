#! /usr/bin/env python

## different sorting algos

arr = [9,8,7,6,5,4,3,2,1]

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
    start = 0
    length = len(arr)
    for idx_in_unsorted in xrange(start + 1, length):
        moving_item = arr[idx_in_unsorted]
        idx_in_sorted = idx_in_unsorted - 1
        while idx_in_unsorted >= 0 and arr[idx_in_sorted] > moving_item:
            arr[idx_in_sorted + 1] = arr[idx_in_sorted]
            idx_in_sorted -= 1



    

print bubble_sort([3,3, 3, 1, 1, 0, -5])