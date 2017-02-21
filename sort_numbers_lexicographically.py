#! /usr/bin/env python3

import math

"""
co: Bloomberg
status: solved
given a number N, print numbers from 1 to N in lexicographic order
e.g., 1 -> 25: 1,10,11,12,....,19,2,20,21,...,25,3,4,5,6,7,8,9
e.g   1 -> 247 1, 10, 100,

1 -> 13

1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9

"""


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return "Value: %d".format(str(self.value))


def print_ll(node):
    res = []
    while node.next != None:
        res.append(node.value)
    res.append(node.value)
    return res


def brute_force(finish):
    if finish <= 9:
        return list(range(1, finish + 1))
    start = Node(1, Node(2))

    for num in range(2, finish + 1):
        to_insert = Node(num)
        cur = start
        print(num, cur.value)
        while str(num) > str(cur.value):
            prev = cur
            cur = cur.next
        to_insert.next = cur
        prev.next = to_insert

    return print_ll(start)

# print(brute_force(10))


def print_from_p_to_s(prefix, suffix):
    """ Called recursively. Given numeric prefix and suffix, 
    print the numbers in a lexicographic order. Returns nothing  """
    # eg. 8431
    if suffix == 0:
        print(prefix)
        return
    if prefix != 0:
        print("finally, a prefix", prefix)

    # 137 is 10**2, but has length 3
    length = int(math.log(suffix, 10)) + 1
    # greatest power of ten that is less than or equal the suffix
    closest_power_of_ten = 10**(length - 1)

    first_digit = int(suffix / closest_power_of_ten)
    # all but the first digit - same order of magnitude
    remainders = suffix - first_digit * closest_power_of_ten
    # order of magnitude one less all nines
    remainders9 = 10**(length - 1) - 1

    # print digits up to the first digit in the number
    for i in range(first_digit):
        if i == 0 and prefix == 0:
            continue
        print_from_p_to_s(10 * prefix + i, remainders9)
    print_from_p_to_s(10 * prefix + first_digit, remainders)

    if remainders9 == 0:
        return

    # print all the numbers with the first digit greater
    # than the first digit of finish
    # eg. 999
    for i in range(first_digit + 1, 10):
        print_from_p_to_s(10 * prefix + i, int(remainders9 / 10))


def recursive_dfs(finish):
    """ 
    Recursive solution using print_from_p_to_s
    """
    # print(1)
    print_from_p_to_s(0, finish)


recursive_dfs(10)
