#! /usr/bin/env python

# -----------
# User Instructions
#
# Define a function smooth that takes a path as its input
# (with optional parameters for weight_data, weight_smooth)
# and returns a smooth path.
#
# Smoothing should be implemented by iteratively updating
# each entry in newpath until some desired level of accuracy
# is reached. The update should be done according to the
# gradient descent equations given in the previous video:
#
# If your function isn't submitting it is possible that the
# runtime is too long. Try sacrificing accuracy for speed.
# -----------


from math import *

# Don't modify path inside your function.
path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]

# ------------------------------------------------
# smooth coordinates
#

def smooth(path, weight_data = 0.5, weight_smooth = 0.1, tolerance=0.000001):

    # Make a deep copy of path into newpath
    newpath = [[0 for col in range(len(path[0]))] for row in range(len(path))]
    for i in range(len(path)):
        for j in range(len(path[0])):
            newpath[i][j] = path[i][j]


    #### ENTER CODE BELOW THIS LINE ###
    iteration_change = float("inf")
    while tolerance < iteration_change:
        temp_path = gradient_descent(path, newpath, weight_data, weight_smooth)
        iteration_change = total_path_change(newpath, temp_path)
        for i in range(len(temp_path)):
            for j in range(len(temp_path[0])):
                newpath[i][j] = temp_path[i][j]
    return newpath

def gradient_descent(path, newpath, weight_data, weight_smooth):
    temp_path = [[0 for component in step] for step in path]
    for i in range(len(path[0])):
        temp_path[0][i] = path[0][i]
    for i in range(len(path[-1])):
        temp_path[-1][i] = path[-1][i]
    for i in range(len(path)):
        if i == 0 or i == len(path) - 1:
            continue
        xi = path[i]
        yi = newpath[i]
        yi = data_update(xi, yi, weight_data)
        yi_sub_1 = newpath[i - 1]
        yi_add_1 = newpath[i + 1]
        temp_path[i] = smooth_update(xi, yi, weight_smooth, yi_sub_1, yi_add_1)
        change_vector = [(j - k) for j, k in zip(newpath[i], temp_path[i])]
    return temp_path

def data_update(xi, yi, weight_data):
    result = vector_subtract(xi, yi)
    result = multiply_scalar_by_vector(weight_data, result)
    result = vector_add(yi, result)
    return result

def smooth_update(xi, yi, weight_smooth, yi_sub_1, yi_add_1):
    result = vector_add(yi_add_1, yi_sub_1)
    result = vector_subtract(result, multiply_scalar_by_vector(2, yi))
    result = multiply_scalar_by_vector(weight_smooth, result)
    result = vector_add(yi, result)
    return result

def vector_subtract(j, k):
    return [ji - ki for ji, ki in zip(j, k)]
def multiply_scalar_by_vector(scalar, vector):
    return [scalar * component for component in vector]
def vector_add(j, k):
    return [ji + ki for ji, ki in zip(j, k)]

def total_path_change(newpath, temp_path):
    total_change = 0
    for i in range(len(newpath)):
        for j in range(len(newpath[0])):
            total_change += abs(newpath[i][j] - temp_path[i][j])
    return total_change

newpath = smooth(path)

# thank you - EnTerr - for posting this on our discussion forum
for i in range(len(path)):
    print '['+ ', '.join('%.3f'%x for x in path[i]) +'] -> ['+ ', '.join('%.3f'%x for x in newpath[i]) +']'
