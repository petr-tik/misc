"""
co: gsa
status: WIP

Given a tree, target Node and an int value X, 
return all nodes X edges away from the target node

A graph is represented as an adjacency hashmap. 
{a: [b,c], b: [d, e], c:[f, g], d:[h]}
"""

z_in_graph = {"a": ["b", "c"], "b": ["d", "e"],
              "c": ["f", "g"], "d": ["h", "z"], "e": [], "f": [], "g": [], "h": [], "z": []}
z_not_in_graph = {"a": ["b", "c"], "b": ["d", "e"],
                  "c": ["f", "g"], "d": ["h", "z"], "f": [], "g": [], "h": []}


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
        print(stack, visited)

    return False

print(node_in_graph(z_in_graph, "z", start="a"))
print(node_in_graph(z_not_in_graph, "z", start="a"))
