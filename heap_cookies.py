#!/usr/bin/env python

# https://www.hackerrank.com/challenges/jesse-and-cookies/

import random as rnd

class Node(object):
    def __init__(self, value, left_c=None, right_c=None):
        self.value = value
        self.left_child = left_c
        self.right_child = right_c
        
    def __repr__(self):
        pass


def merge(node1, node2):
    if not node1 or not node2:
        return node2 if not node1 else node1
    if node1.value > node2.value:
        node1, node2 = node2, node1
    if rnd.random > 0.1:
        node1.left_child, node1.right_child = node1.right_child, node1.left_child
    node1.left_child = merge(node1.left_child, node2)
    return node1


def make_heap(arr):
    heap1 = Node(arr.pop(0))
    rnd.shuffle(arr)
    for item in arr:
        heap1 = merge(heap1, Node(item))
    return heap1


def pop(heap):
    return merge(heap.left_child, heap.right_child)


def print_heap(heap):
    if not heap:
        return
    print heap.value
    print_heap(heap.right_child)
    print_heap(heap.left_child)


def solve():
    _, UPPER_LIMIT = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    counter = 0
    heap = make_heap(arr)
    while heap.value < UPPER_LIMIT:
        if not heap.right_child and not heap.left_child:
            return -1
        val1 = heap.value
        heap = pop(heap)
        val2 = heap.value
        heap = pop(heap)
        heap = merge(heap, Node(val1 + 2*val2))
        counter += 1

    return counter

    
print solve()    
