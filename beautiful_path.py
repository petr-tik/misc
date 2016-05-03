#! usr/bin/env python

# https://www.hackerrank.com/challenges/beautiful-path


def make_graph():
    N, M = [int(x) for x in raw_input().split()]
    graph = {}
    for _ in xrange(M):
        start, finish, cost = [int(x) for x in raw_input().split()]
        if not graph.has_key(start):
            graph[start] = [(finish, cost)]
        else:
            graph[start].append((finish, cost))
    return graph

def dec_to_binary(costs):
    # given a path with decimal cost values, 
    # result in binary strings of same length 
    costs_bin = []
    for cost in costs:
        cost_bin = bin(cost)[2:]
        full_num = '0'*(11 - len(cost_bin)) + cost_bin
        costs_bin.append(full_num)
    return costs_bin

def bitwise_or(binary_strings):
    # given a list of binary values, return the result of bitwise or on them
    res = ['0' for _ in xrange(11)]
    for num in binary_strings:
        for idx, bit in enumerate(num):
            if bit == '1':
                res[idx] = '1'
    return int("".join(res), 2)


def find_paths(graph, start, finish):
    pass    




def min_path(paths):
    res = 1000000000000
    for path in paths:
        if bitwise_or(path) < res:
            res = bitwise_or(path)
    return res



def solve(graph, start, finish):
    paths = find_paths(graph, start, finish)
    if len(paths) == 0:
        print "-1"
    elif len(paths) == 1:
        print bitwise_or(paths[0])
    else:
        print min_path(paths)


print bitwise_or(dec_to_binary([5,4,1024]))
