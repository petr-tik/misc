#! usr/bin/env python

# https://www.hackerrank.com/challenges/candies

import random

ratings_spec = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
ratings_new = [4, 6, 10, 9, 7, 5, 3, 4, 12, 19, 17, 13]


def prepare_for_bfs(ratings):
    """ Given an array of students' grades, 
    return:
        an array of nodes adjacent to each node
        an array of indices with nodes without incoming edges - 
            they will be the start to bfs
    """
    # turn the ratings array into a list of adjacency lists
    graph_list = [[] for _ in xrange(len(ratings))]
    # number of incoming edges to node with index i
    in_edges = [0 for _ in ratings]
    for idx in xrange(0, len(ratings) - 1):
        cur = ratings[idx]
        next = ratings[idx + 1]
        if next > cur:
            graph_list[idx].append(idx + 1)
            in_edges[idx + 1] += 1
        elif cur > next:
            graph_list[idx + 1].append(idx)
            in_edges[idx] += 1

    # use the edges
    start = [idx for idx, item in enumerate(in_edges) if item == 0]
    return graph_list, start


def bfs(ratings, graph, start):
    """ Perform problem-specific bfs on the given array of ratings/grades 
    with a pre-calculated array of indices to start from.  
    """
    candies = [-1 for _ in ratings]
    for idx in start:
        candies[idx] = 1
    cur = start
    while cur:
        next_gen = []
        for from_node in cur:
            for to_node in graph[from_node]:
                if candies[to_node] == -1:  # not visited yet
                    # if not visited, put into the list for starting next
                    # iteration
                    next_gen.append(to_node)
                # the next vertex will have value at least 1 greater than the
                # previous
                candies[to_node] = candies[from_node] + 1
        cur = next_gen

    return candies


def solve(ratings):
    print ratings
    graph, start = prepare_for_bfs(ratings)
    return bfs(ratings, graph, start)

for _ in xrange(5):
    ratings = [random.randint(1, 20) for _ in xrange(10)]
    candies = solve(ratings)
    print sum(candies)
