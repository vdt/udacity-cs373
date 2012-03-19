#! /usr/bin/env python

# ----------
# User Instructions:
#
# Create a function optimum_policy() that returns
# a grid which shows the optimum policy for robot
# motion. This means there should be an optimum
# direction associated with each navigable cell.
#
# un-navigable cells must contain an empty string
# WITH a space, as shown in the previous video.
# Don't forget to mark the goal with a '*'

# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
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

def named_neighbors(i, j):
    bros = []
    for h in range(len(delta)):
        di, dj = delta[h]
        name = delta_name[h]
        bros.append([[i + di, j + dj], name])
    return bros

def valid_neighbors_name_value(i, j, closed, value):
    bros = []
    for [p, q], name in named_neighbors(i, j):
        if valid_cell(p, q, closed):
            bros.append([name, value[p][q]])
    return bros

def minimum_neighbor_name(i, j, closed, value):
    bros = []
    minimum_name = ' '
    minimum = 99
    for name, value in valid_neighbors_name_value(i, j, closed, value):
        if value < minimum:
            minimum = value
            minimum_name = name
    return minimum_name

def optimum_policy():
    value = compute_value()
    policy = [[' ' for cell in row] for row in grid]
    closed = [[False if cell == 0 else True for cell in row] for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if valid_cell(i, j, closed):
                policy[i][j] = minimum_neighbor_name(i, j, closed, value)
    policy[goal[0]][goal[1]] = '*'
    return policy
