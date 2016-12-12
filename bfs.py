#! /usr/bin/env python

from collections import deque


def bfs(G, start, finish):
    """ Implementing an iterative Breadth-First Search on undirected graphs. 
    Takes Graph and returns the length of the path between start and finish, 
    -1 - if no path between the 2. """
    if start == finish:
        return 0  # edge case - going to myself is 0
    marked = set()
    queue = deque()
    marked.add(start)
    queue.append((start, 0))
    while queue:
        cur, cur_depth = queue.popleft()
        children = G[cur]
        for child in children:
            if child == finish:
                return cur_depth + 1
            elif child not in marked:
                marked.add(child)
                queue.append((child, cur_depth + 1))
    return -1  # exhausted the whole queue and no path
