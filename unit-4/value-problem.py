#! /usr/bin/env python

# ----------
# User Instructions:
#
# Create a function compute_value() which returns
# a grid of values. Value is defined as the minimum
# number of moves required to get from a cell to the
# goal.
#
# If it is impossible to reach the goal from a cell
# you should assign that cell a value of 99.

# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost_step = 1 # the cost associated with moving from a cell to an adjacent one.

# ----------------------------------------
# insert code below
# ----------------------------------------
def neighbors(i, j):
    return [[i + di, j + dj] for di, dj in delta]

def in_grid(i, j):
    return i in range(len(grid)) and j in range(len(grid[0]))

def valid_cell(i, j, closed):
    return in_grid(i, j) and not closed[i][j]

def valid_neighbors(i, j, closed):
    return [[p, q] for p, q in neighbors(i, j) if valid_cell(p, q, closed)]

def recursive_value_grid(open, closed, value_grid):
    open.sort()
    if open:
        value, [i, j] = open[0]
        value_grid[i][j] = value
        value_prime = value + cost_step
        for p, q in valid_neighbors(i, j, closed):
            closed[p][q] = True
            open.append([value_prime, [p, q]])
        return recursive_value_grid(open[1:], closed, value_grid)
    else:
        return value_grid

def compute_value():
    closed = [[False if cell == 0 else True for cell in row] for row in grid]
    closed[goal[0]][goal[1]] = True
    value_grid = [[99 for cell in row] for row in grid]
    value = 0
    open = [[value, goal]]

    return recursive_value_grid(open, closed, value_grid)
