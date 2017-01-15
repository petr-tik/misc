#! /usr/bin/env python3

"""
Given a grid of colour values at different cells and a new colour Y.

Turn a given pixel (x, y) and all neighbouring cells of the same colour into colour Y and return the new grid. Assume neighbouring cells are the ones that share an edge

Solution ideas:
Recursive bfs with starting (x, y) as start and all its neighbours as children. When traversing only colour the same-colour children as the parent.

"""


def matrix_index(matrix, index_tuple):
    """ Input:
                a matrix (array of arrays)
                coordinates (tuple of 2 elements)
        Output:
                value at given index, if present
                IndexError, if absent
    """
    try:
        return matrix[index_tuple[0]][index_tuple[1]]
    except IndexError:
        raise IndexError


test_matrix = [[0 for _ in range(3)], [1 for _ in range(3)], [
    2 for _ in range(3)], [3 for _ in range(3)]]
print(matrix_index(test_matrix, (1, 2)))
