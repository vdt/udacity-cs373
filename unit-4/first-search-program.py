#! /usr/bin/env python

# ----------
# User Instructions:
#
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def search():
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------
    blocked = [[False if cell == 0 else True for cell in row] for row in grid]
    init_g_value = 0
    open = [[init_g_value, init]]
    while open:
        open.sort()
        open.reverse()
        now = open.pop()
        now_g_value = now[0]
        now_coordinates = now[1]
        now_i, now_j = now_coordinates
        if now_coordinates == goal:
            return [now_g_value, now_i, now_j]
        blocked[now_i][now_j] = True
        new_g_value = now_g_value + cost
        for delta_i, delta_j in delta:
            new_i, new_j = [now_i + delta_i, now_j + delta_j]
            new = [new_g_value, [new_i, new_j]]
            if new_i in range(len(grid)) and new_j in range(len(grid[0])) and \
                    not blocked[new_i][new_j]:
                open.append(new)
    return 'fail'
print search()
