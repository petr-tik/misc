#! usr/bin/env python

# https://www.hackerrank.com/challenges/candies

import random

"""
N = int(raw_input())

candies = [1 for _ in xrange(N)]


ratings = []
for _ in xrange(N):
    ratings.append(int(raw_input()))
"""
# print len(candies), candies

candies = [1 for _ in xrange(10)]

ratings = [random.randint(1,20) for _ in xrange(10)]

ratings_spec = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
ratings_new = [4, 6, 10, 9, 7, 5, 3, 4, 12, 19, 17, 13]

def make_graph(ratings):
    # turn the ratings array into a list of adjacency lists
    graph_list = [[] for _ in xrange(len(ratings))]
    in_edges = [0 for _ in ratings] # number of incoming edges to node with index i 
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

graph, start = make_graph(ratings_spec)

def bfs(ratings, graph, start):    
    candies = [-1 for _ in ratings] 
    for idx in start:
        candies[idx] = 1
    cur = start
    while cur:
        next_gen = []
        for from_node in cur:
            for to_node in graph[from_node]:
                if candies[to_node] == -1: # not visited yet
                    next_gen.append(to_node)
                candies[to_node] = candies[from_node] + 1
        cur = next_gen

    return sum(candies)

print bfs(ratings_spec, graph, start)

print ratings_spec
# print make_graph([4, 5, 6, 6, 7])


#print "We need to buy {} candies".format(candy_calc(ratings))
#print ratings_spec
#print "We need to buy {} candies".format(candy_calc(ratings_spec))
