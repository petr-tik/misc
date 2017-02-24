#! /usr/bin/env python2


""" A bipartite graph is one, where each node belongs to either of 2 sets,
such that no 2 nodes in the same set are adjacent.

Given a graph, return True if it's bipartite, False otherwise

Graphs are represented as adjacency dictionaries with digits for nodes

"""

import collections

# test_bipartite = {1: [4, 5, 6], 2: [4, 5, 6], 3: [4, 5, 6],
#                   4: [1, 2, 3], 5: [1, 2, 3], 6: [1, 2, 3]}

test_bipartite = {1: [2, 3], 2: [1, 4], 3: [1, 3], 4: [2, 3]}
test_not_bipartite = {digit: list(range(7)) for digit in range(7)}

# 1: [4, 5, 6], 2: [4, 5, 6], 3: [4, 5, 6],
#                       4: [1, 2, 3], 5: [1, 2, 6], 6: [1, 5, 3]}


def is_bipartite(graph, start=1):
    """ Check if a graph is bipartite using the helper bfs"""
    queue = collections.deque([start])
    return bfs(graph, queue)


def bfs(graph, queue, visited=set(), counter=0, set_a=[], set_b=[]):
    """ Given a graph and a starting point,
    return True if bipartite, false otherwise"""
    while queue:
        cur = queue.popleft()
        if cur == None:
            counter += 1
            return bfs(graph, queue, visited, counter, set_a, set_b)
        visited.add(cur)
        children = graph[cur]
        eligible_children = [child for child in children
                             if child not in queue and child not in visited]
        print(eligible_children)
        if counter % 2 == 0:
            if any(child in set_a for child in children):
                print cur, children, set_a, counter
                return False
            else:
                set_b.extend(eligible_children)
                queue.extend(eligible_children)
                queue.append(None)
                return bfs(graph, queue, visited, counter, set_a, set_b)
        elif counter % 2 == 1:
            if any(child in set_b for child in children):
                print cur, children, set_a, counter
                return False
            else:
                set_a.extend(eligible_children)
                queue.extend(eligible_children)
                return bfs(graph, queue, visited, counter, set_a, set_b)
    return True


def check():
    print(is_bipartite(test_bipartite, 1))
    print(is_bipartite(test_not_bipartite, 4))

check()
