#! /usr/bin/env python

# ----------
# User Instructions:
#
# Implement the function optimum_policy2D() below.
#
# You are given a car in a grid with initial state
# init = [x-position, y-position, orientation]
# where x/y-position is its position in a given
# grid and orientation is 0-3 corresponding to 'up',
# 'left', 'down' or 'right'.
#
# Your task is to compute and return the car's optimal
# path to the position specified in `goal'; where
# the costs for each motion are as defined in `cost'.

# EXAMPLE INPUT:

# grid format:
#     0 = navigable space
#     1 = occupied space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]
goal = [2, 0] # final position
init = [4, 3, 0] # first 2 elements are coordinates, third is direction
cost = [2, 1, 20] # the cost field has 3 values: right turn, no turn, left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D() should return the array
#
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
#
# ----------


# there are four motion directions: up/left/down/right
# increasing the index in this array corresponds to
# a left turn. Decreasing is is a right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # do right
forward_name = ['up', 'left', 'down', 'right']

# the cost field has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']


# ----------------------------------------
# modify code below
# ----------------------------------------

def neighbors(i, j, theta):
    bros = []
    for action_index in range(len(action)):
        act = action[action_index]
        theta_prime = (theta + act) % len(forward)
        di, dj = forward[theta_prime]
        bros.append([action_index, [i + di, j + dj, theta_prime]])
    return bros

def in_grid(i, j, theta):
    return i in range(len(grid)) and j in range(len(grid[0])) \
        and theta in range(len(forward))

def valid_cell(i, j, theta, closed):
    return in_grid(i, j, theta) and not closed[theta][i][j]

def valid_neighbors(i, j, theta, closed):
    bros = []
    for action_index, [p, q, theta_prime] in neighbors(i, j, theta):
        if valid_cell(p, q, theta_prime, closed):
            bros.append([action_index, [p, q, theta_prime]])
    return bros

def initial_closed():
    return [[[False if cell == 0 else True for cell in row] for row in grid] \
                for direction in forward]

def recursive_path(open, closed):
    open.sort()
    g, [i, j, theta], trail = open[0]
    closed[theta][i][j] = True
    if [i, j] == goal:
        return trail
    else:
        for action_index, [p, q, theta_prime] in \
                valid_neighbors(i, j, theta, closed):
            act = action[action_index]
            g_prime = g + cost[action_index]
            new_trail = trail + [[action_index, [i, j]]]
            open.append([g_prime, [p, q, theta_prime], new_trail])
        return recursive_path(open[1:], closed)

def optimum_policy2D():
    policy = [[' ' for cell in row] for row in grid]
    g = 0
    i, j, theta = init
    closed = initial_closed()
    closed[theta][i][j] = True
    open = [[g, init, []]]
    path = recursive_path(open, closed)
    for act, [i, j] in path:
        policy[i][j] = action_name[act]
    policy[goal[0]][goal[1]] = '*'
    return policy
