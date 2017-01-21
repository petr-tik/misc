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


def find_neighbour_coords(coord):
    right = (coord[0], coord[1] + 1)
    left = (coord[0], coord[1] - 1)
    up = (coord[0] + 1, coord[1])
    down = (coord[0] - 1, coord[1])
    return [right, left, up, down]


def find_same_colour_adjacent(matrix, coord):
    """ Given a matrix and a tuple of coordinates,
    return an array of coordinate tuples of pixels with the same colour as coord"""
    coordinates = []
    colour = getAtIndex(matrix, coord)  # current target colour
    cand_coords = find_neighbour_coords(coord)
    for coord in cand_coords:
        try:
            next_colour = getAtIndex(matrix, coord)
            if next_colour == colour:
                coordinates.append(coord)
        except IndexError:
            pass
            # do nothing on IndexError - just ignore the coordinates out of
            # bounds
    return coordinates


def colour_matrix(matrix, cur, new_colour, visited=set()):
    """ Input:
    a matrix of colour-values,
    new colour value
    and a tuple of coordinates,
    colour all pixels neighbouring the tuple of coordinates into the new colour

    Output:
    a matrix with new colours
    """
    visited.add(cur)
    children = find_same_colour_adjacent(matrix, cur)
    # print(children)
    setAtIndex(matrix, cur, new_colour)
    for child in children:
        if child not in visited:
            colour_matrix(matrix, child, new_colour, visited)

    return matrix


def solve():
    test_m = [[0, 0, 5, 0], [5, 0, 5, 0], [5, 5, 5, 5], [0, 0, 0, 0]]
    res = [[0, 0, 9, 0], [9, 0, 9, 0], [9, 9, 9, 9], [0, 0, 0, 0]]
    print(res == colour_matrix(test_m, (0, 2), 9))

solve()
