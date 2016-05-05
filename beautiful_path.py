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
    # assertEqual(N, len(graph))
    return graph

def dec_to_binary(costs):
    # given a path with decimal cost values, 
    # return binary strings of uniform length 11 chars
    costs_bin = []
    for cost in costs:
        cost_bin = bin(cost)[2:]
        full_num = '0'*(11 - len(cost_bin)) + cost_bin
        costs_bin.append(full_num)
    return costs_bin

def bitwise_or(binary_strings):
    # given a list of binary value strings, return the integer result of 'bitwise or'
    # bitwise or compares >=2 binary numbers of the same length bit by bit,
    # assigning 1 to the result if at least one of the bits is 1
    # eg
    #           101001
    #           010110
    # result:   111111
    res = ['0' for _ in xrange(11)]
    for num in binary_strings:
        for idx, bit in enumerate(num):
            if bit == '1':
                res[idx] = '1' # else it will still be 0
    return int("".join(res), 2)

def find_paths(graph, start, finish, path=[]):
    path = path + [start]
    if start == finish:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node[0] not in path:
            newpaths = find_paths(graph, node[0], finish, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def find_min_path(paths):
    res = -1
    for path in paths:
        if res == -1 or bitwise_or(path) < res:
            res = bitwise_or(path)
    return res


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