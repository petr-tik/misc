#! /usr/bin/env python3

"""
co: Bloomberg
status: WIP
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

print(brute_force(10))


def recursive_solution(finish, tree):
    """ Recursive solution using trees 
    log(finish, 10) determines the depth of tree
    if depth > x, all levels above x are complete

    """
    if finish <= 9:
        return list(range(1, finish + 1))
    if res == {}:
        res = {str(k): [] for k in range(1, 10)}


def print_tree(root):
    """ Given a tree 
            x
          /  \
         y    z

    print x, xy, xz
    """
