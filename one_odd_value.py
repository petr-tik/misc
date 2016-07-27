#! /usr/bin/env python

""" 
Given an array of ints, where all but one value appear even number of times
return the value that appears odd number of times

"""

test1 = [1,1,1,1,3]
test2 = [4,5,6,4,5]

def solve_with_hash(arr):
    """ Hashmap implementation: needs 2 runs through the array
    First make a counter hashmap of values and their counts, 
    then find the value, whose count is odd - return
    """
    counter = {}
    for element in arr:
        if element in counter:
            counter[element] += 1
        else:
            counter[element] = 1

    for key in counter:
        if counter[key] % 2 == 1:
            return key


def solve_with_xor(arr):
    """ XOR all elements with each other. 
    All the values that appear an even number of times will produce 0, 
    the only element appearing an odd number of times gives itself
    4 XOR 4 = 0
    4 XOR 4 XOR 5 = 5

    """
    res = 0
    for element in arr:
        res ^= element
    return res

print solve_with_hash(test1)
print solve_with_xor(test1)
