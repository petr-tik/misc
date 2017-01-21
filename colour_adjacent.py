#! /usr/bin/env python3

"""
Given a grid of colour values at different cells and a new colour Y.

Turn a given pixel (x, y) and all neighbouring cells of the same colour into colour Y and return the new grid. Assume neighbouring cells are the ones that share an edge

Solution ideas:
Recursive bfs with starting (x, y) as start and all its neighbours as children. When traversing only colour the same-colour children as the parent.

"""


def getAtIndex(matrix, index_tuple):
    """ Input:
                a matrix (array of arrays)
                coordinates (tuple of 2 elements)
                    tuple is of the form (y, x)
        Output:
                value at given index, if present
                IndexError, if absent
    """
    try:
        res = matrix[index_tuple[1]][index_tuple[0]]
        return res
    except IndexError:
        raise IndexError


def setAtIndex(matrix, index_tuple, new_val):
    """ Input:
                a matrix (array of arrays)
                coordinates (tuple of 2 elements)
                    tuple is of the form (y, x)
        Output:
               nothing, changes value in matrix inplace
    """
    try:
        matrix[index_tuple[1]][index_tuple[0]] = new_val
    except IndexError:
        raise IndexError
    colour all pixels neighbouring the tuple of coordinates into the new colour

    Output:
    a matrix with new colours
    """
    pass
