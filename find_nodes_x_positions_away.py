"""
co: gsa
status: done

Given a tree, target Node and an int value X, 
return all nodes X edges away from the target node

A graph is represented as an adjacency hashmap. 
{a: [b,c], b: [d, e], c:[f, g], d:[h]}
"""

z_in_graph = {"a": ["b", "c"], "b": ["a", "d", "e"],
              "c": ["a", "f", "g"], "d": ["b", "h", "z"],
              "e": ["b"], "f": ["c"], "g": ["c"], "h": ["d"], "z": ["d"]}
z_not_in_graph = {"a": ["b", "c"], "b": ["a", "d", "e"],
                  "c": ["a", "f", "g"], "d": ["b", "h"],
                  "e": [], "f": ["c"], "g": ["c"], "h": []}


def node_in_graph(graph, target_node, start=None, visited=set()):
    """ Given a graph, return False, if target node not in graph.
    else, return True. Using depth-first search.
    """
    if start == target_node:
        return True
    stack = list(start)

    while stack:
        cur = stack.pop()
        visited.add(cur)
        for child in graph[cur]:
            if child == target_node:
                return True
            if child not in visited:
                stack.append(child)

    return False

print(node_in_graph(z_in_graph, "z", start="a"))
print(node_in_graph(z_not_in_graph, "z", start="a"))


def nodes_at_distance(graph, dist, start, res=list(), visited=set()):
    """
    Input:
    - graph as an adjacency hashmap
    - start - node to start with
    - distance - integer how many edges away from the target_node

    Return:
    - array of vertices `dist` edges away from the start
    (array may be empty)

    Called recursively with a decreasing distance var. 
    Nodes that you reach with distance of 0, are the ones you need.
    """
    visited.add(start)
    if dist == 0 or:
        res.append(start)
        return res
    for child in graph[start]:
        if child not in visited:
            res = nodes_at_distance(graph, dist - 1, child, res, visited)
    return res

print(nodes_at_distance(z_in_graph, 3, "z"))
