#! /usr/bin/env python

# -----------
# User Instructions:
#
# Modify the the search function so that it becomes
# an A* search algorithm as defined in the previous
# lectures.
#
# Your function should return the expanded grid
# which shows, for each element, the count when
# it was expanded or -1 if the element was never expanded.
#
# Your function only needs to work for a 5x6 grid.
# You do not need to modify the heuristic.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

heuristic = [[9, 8, 7, 6, 5, 4],
            [8, 7, 6, 5, 4, 3],
            [7, 6, 5, 4, 3, 2],
            [6, 5, 4, 3, 2, 1],
            [5, 4, 3, 2, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

# ----------------------------------------
# modify code below
# ----------------------------------------

def neighbors(i, j):
    return [[i + di, j + dj] for di, dj in delta]

def in_grid(i, j):
    return i in range(len(grid)) and j in range(len(grid[0]))

def valid_cell(i, j, closed):
    return in_grid(i, j) and not closed[i][j]

def valid_neighbors(i, j, closed):
    return [[p, q] for p, q in neighbors(i, j) if valid_cell(p, q, closed)]

def recursive_expand(open, closed, expand, expansion_count):
    open.sort()
    f, g, [i, j] = open[0]
    expand[i][j] = expansion_count
    if [i, j] == goal:
        return expand
    else:
        g_prime = g + cost
        for p, q in valid_neighbors(i, j, closed):
            closed[p][q] = True
            f_prime = g_prime + heuristic[p][q]
            open.append([f_prime, g_prime, [p, q]])
        return recursive_expand(open[1:], closed, expand, expansion_count + 1)

def search():
    closed = [[False if cell == 0 else True for cell in row] for row in grid]
    closed[init[0]][init[1]] = True

    expand = [[-1 for cell in row] for row in grid]
    expansion_count = 0

    i, j = init
    g = 0
    f = g + heuristic[i][j]

    open = [[f, g, init]]

    return recursive_expand(open, closed, expand, expansion_count)
