#! /usr/bin/env python

# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that 
# takes no input and RETURNS two grids. The
# first grid, value, should contain the computed
# value of each cell as shown in the video. The
# second grid, policy, should contain the optimum
# policy for each cell.
#
# Stay tuned for a homework help video! This should
# be available by Thursday and will be visible
# in the course content tab.
#
# Good luck! Keep learning!
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.
#
# NOTE: Please do not modify the values of grid,
# success_prob, collision_cost, or cost_step inside
# your function. Doing so could result in your
# submission being inappropriately marked as incorrect.

# -------------
# GLOBAL VARIABLES
#
# You may modify these variables for testing
# purposes, but you should only modify them here.
# Do NOT modify them inside your stochastic_value
# function.

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
goal = [0, len(grid[0])-1] # Goal is in top right corner

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

success_prob = 0.5
# Probability(stepping left) = prob(stepping right) = failure_prob
failure_prob = (1.0 - success_prob)/2.0
collision_cost = 100
cost_step = 1
############## INSERT/MODIFY YOUR CODE BELOW ##################
#
# You may modify the code below if you want, but remember that
# your function must...
#
# 1) ...be called stochastic_value().
# 2) ...NOT take any arguments.
# 3) ...return two grids: FIRST value and THEN policy.

def print_table(table):
    for row in table:
        print row

def initial_values():
    values = []
    for i in range(len(grid)):
        values.append([])
        for j in range(len(grid[0])):
            if [i, j] == goal:
                values[i].append(0.0)
            else:
                values[i].append(1000.0)
    return values

def initial_policy():
    policy = []
    for i in range(len(grid)):
        policy.append([])
        for j in range(len(grid[0])):
            if [i, j] == goal:
                policy[i].append('*')
            else:
                policy[i].append(' ')
    return policy

def initial_walls():
    return [[True if cell == 1 else False for cell in row] for row in grid]

def neighbors(i, j, delta_index):
    bros = []
    for delta_delta in [0, 1, -1]:
        delta_prime = (delta_index + delta_delta) % len(delta)
        di, dj = delta[delta_prime]
        bros.append([i + di, j + dj])
    return bros

def in_grid(i, j):
    return i in range(len(grid)) and j in range(len(grid[0]))

def collision(i, j, walls):
    return (not in_grid(i, j)) or walls[i][j]

def values(cells, value, walls):
    bro_values = []
    for cell in cells:
        i, j = cell
        if collision(i, j, walls):
            bro_values.append(collision_cost)
        else:
            bro_values.append(value[i][j])
    return bro_values

def neighbor_values(i, j, delta_index, value, walls):
    return values(neighbors(i, j, delta_index), value, walls)

def state_action_value(i, j, action_index, value, walls):
    bro_values = neighbor_values(i, j, action_index, value, walls)
    return success_prob * bro_values[0] + failure_prob * sum(bro_values[1:]) + 1

def state_value(i, j, value, walls):
    action_values = []
    for action_index in range(len(delta)):
        action_value = state_action_value(i, j, action_index, value, walls)
        action_values.append(action_value)
    return min(action_values)

def update_values(value, walls):
    values_prime = []
    for i in range(len(value)):
        values_prime.append([])
        for j in range(len(value[0])):
            if collision(i, j, walls) or [i, j] == goal:
                value_prime = value[i][j]
            else:
                value_prime = state_value(i, j, value, walls)
            values_prime[i].append(value_prime)
    return values_prime

def maximum_change(values, values_prime):
    max_change = 0.0
    for row, row_prime in zip(values, values_prime):
        for cell, cell_prime in zip(row, row_prime):
            change = abs(cell - cell_prime)
            if max_change < change:
                max_change = change
    return max_change

def stochastic_value():
    value = initial_values()
    policy = initial_policy()
    walls = initial_walls()

    value_prime = update_values(value, walls)

    while maximum_change(value, value_prime) > 0.0001:
        value = value_prime
        value_prime = update_values(value, walls)
    print "value ="
    print_value_table(value)

    return value, policy

def print_value_table(value_table):
    for row in value_table:
        for cell in row:
            print "%0.3f" % cell,
        print

stochastic_value()
