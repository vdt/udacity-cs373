#! /usr/bin/env python

# -----------
# User Instructions:
# 
# Modify the function search() so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# For grading purposes, please leave the return
# statement at the bottom.
# ----------


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]

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

def in_grid(i, j):
    return i in range(len(grid)) and j in range(len(grid[0]))

def search():
    expand = [[-1 for cell in row] for row in grid]
    closed = [[False if cell == 0 else True for cell in row] for row in grid]
    closed[init[0]][init[1]] = True
    expanded_at = 0

    open = [init]

    while open:
        open.sort()
        open.reverse()
        i, j = open.pop()
        expand[i][j] = expanded_at
        expanded_at += 1

        for delta_i, delta_j in delta:
            new_i, new_j = i + delta_i, j + delta_j
            if in_grid(new_i, new_j) and not closed[new_i][new_j]:
                open.append([new_i, new_j])
                closed[new_i][new_j] = True
    return expand #Leave this line for grading purposes!
