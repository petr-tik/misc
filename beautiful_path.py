#! usr/bin/env python

from collections import deque

# https://www.hackerrank.com/challenges/beautiful-path

# Turn the graph into unweighted, so you can run bfs on it. 
# There are only 2**10 binary lengths between 2 vertices
# Turn 
#
#
#

def make_graph():
    N, M = [int(x) for x in raw_input().split()]
    graph = {}
    for _ in xrange(M):
        start, finish, cost = [int(x) for x in raw_input().split()]
        if not graph.has_key(start):
            graph[start] = [(finish, cost)]
        else:
            graph[start].append((finish, cost))
    # assertEqual(N, len(graph))
    return graph


def bfs(graph, start):
    dist = [-1 for _ in xrange(len(graph))]
    dist[start] = 0
    q = deque([]) # make a queue from deque object
    q.appendleft(start)
    while q:
        v = q.pop() # study the first out element from queue
        for idx in xrange(len(graph[v])): # all v's children indices
            v2 = g[v][idx] # each child 
            if dist[v2] == -1: # still hasn't been visited
                dist[v2] = dist[v] + 1 # to get to the child we need one more step than to parent
                q.appendleft(v2)



def solve(graph, start, finish):
    paths = find_paths(graph, start, finish)
    if len(paths) == 0:
        print "-1"
    elif len(paths) == 1:
        print bitwise_or(dec_to_binary(paths[0]))
    else:
        print find_min_path(paths)


print bitwise_or(dec_to_binary([5,4,1024]))

# graph = make_graph()
# start = raw_input()
# 

# print make_graph()
solve(make_graph(), 1, 3)