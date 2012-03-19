#! /usr/bin/env python

# ----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
#
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left,
# up, and down motions. NOTE: the 'v' should be
# lowercase.
#
# Your function should be able to do this for any
# provided grid, not just the sample grid below.
# ----------


# Sample Test case
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]

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
    bros = []
    for h in range(len(delta)):
        di, dj = delta[h]
        bro = [delta_name[h], [i + di, j + dj]]
        bros.append(bro)
    return bros

def in_grid(i, j):
    return i in range(len(grid)) and j in range(len(grid[0]))

def valid_neighbors(i, j, closed):
    bros = []
    for name, [p, q] in neighbors(i, j):
        if in_grid(p, q) and not closed[p][q]:
            bros.append([name, [p, q]])
    return bros

def search():
    map = [[' ' for cell in row] for row in grid]
    map[goal[0]][goal[1]] = '*'
    closed = [[False if cell == 0 else True for cell in row] for row in grid]
    closed[init[0]][init[1]] = True
    g = 0

    trail = []
    open = [[g, init, trail]]

    while open:
        open.sort()
        open.reverse()
        g, [i, j], trail = open.pop()
        if [i, j] == goal:
            break
        g += cost
        for name, [p, q] in valid_neighbors(i, j, closed):
            new_trail = trail + [[name, [i, j]]]
            open.append([g, [p, q], new_trail])
            closed[p][q] = True
    for name, [i, j] in trail:
        map[i][j] = name
    return map # make sure you return the shortest path.
