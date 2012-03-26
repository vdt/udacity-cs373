#! /usr/bin/env python

# -------------
# User Instructions
#
# Here you will be implementing a cyclic smoothing
# algorithm. This algorithm should not fix the end
# points (as you did in the unit quizzes). You  
# should use the gradient descent equations that
# you used previously.
#
# Your function should return the newpath that it
# calculates..
#
# Feel free to use the provided solution_check function
# to test your code. You can find it at the bottom.
#
# --------------
# Testing Instructions
# 
# To test your code, call the solution_check function with
# two arguments. The first argument should be the result of your
# smooth function. The second should be the corresponding answer.
# For example, calling
#
# solution_check(smooth(testpath1), answer1)
#
# should return True if your answer is correct and False if
# it is not.

from math import *

# Do not modify path inside your function.
path=[[0, 0], 
      [1, 0],
      [2, 0],
      [3, 0],
      [4, 0],
      [5, 0],
      [6, 0],
      [6, 1],
      [6, 2],
      [6, 3],
      [5, 3],
      [4, 3],
      [3, 3],
      [2, 3],
      [1, 3],
      [0, 3],
      [0, 2],
      [0, 1]]

############# ONLY ENTER CODE BELOW THIS LINE ##########

# ------------------------------------------------
# smooth coordinates
# If your code is timing out, make the tolerance parameter
# larger to decrease run time.
#

def smooth(path, weight_data = 0.1, weight_smooth = 0.1, tolerance = 0.00001):

    # 
    # Enter code here
    #
    newpath = [[0 for component in step] for step in path]
    for i in range(len(path)):
        for j in range(len(path[0])):
            newpath[i][j] = path[i][j]
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
    for i in range(len(path)):
        xi = path[i]
        yi = newpath[i]
        yi = data_update(xi, yi, weight_data)
        yi_sub_1 = newpath[(i - 1) % len(newpath)]
        yi_add_1 = newpath[(i + 1) % len(newpath)]
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

# thank you - EnTerr - for posting this on our discussion forum

#newpath = smooth(path)
#for i in range(len(path)):
#    print '['+ ', '.join('%.3f'%x for x in path[i]) +'] -> ['+ ', '.join('%.3f'%x for x in newpath[i]) +']'


##### TESTING ######

# --------------------------------------------------
# check if two numbers are 'close enough,'used in
# solution_check function.
#
def close_enough(user_answer, true_answer, epsilon = 0.001):
    if abs(user_answer - true_answer) > epsilon:
        return False
    return True

# --------------------------------------------------
# check your solution against our reference solution for
# a variety of test cases (given below)
#
def solution_check(newpath, answer):
    if type(newpath) != type(answer):
        print "Error. You do not return a list."
        return False
    if len(newpath) != len(answer):
        print 'Error. Your newpath is not the correct length.'
        return False
    if len(newpath[0]) != len(answer[0]):
        print 'Error. Your entries do not contain an (x, y) coordinate pair.'
        return False
    for i in range(len(newpath)): 
        for j in range(len(newpath[0])):
            if not close_enough(newpath[i][j], answer[i][j]):
                print 'Error, at least one of your entries is not correct.'
                return False
    print "Test case correct!"
    return True

# --------------
# Testing Instructions
# 
# To test your code, call the solution_check function with
# two arguments. The first argument should be the result of your
# smooth function. The second should be the corresponding answer.
# For example, calling
#
# solution_check(smooth(testpath1), answer1)
#
# should return True if your answer is correct and False if
# it is not.
    
testpath1 = [[0, 0],
             [1, 0],
             [2, 0],
             [3, 0],
             [4, 0],
             [5, 0],
             [6, 0],
             [6, 1],
             [6, 2],
             [6, 3],
             [5, 3],
             [4, 3],
             [3, 3],
             [2, 3],
             [1, 3],
             [0, 3],
             [0, 2],
             [0, 1]]

answer1 = [[0.5449300156668018, 0.47485226780102946],
           [1.2230705677535505, 0.2046277687200752],
           [2.079668890615267, 0.09810778721159963],
           [3.0000020176660755, 0.07007646364781912],
           [3.9203348821839112, 0.09810853832382399],
           [4.7769324511170455, 0.20462917195702085],
           [5.455071854686622, 0.4748541381544533],
           [5.697264197153936, 1.1249625336275617],
           [5.697263485026567, 1.8750401628534337],
           [5.455069810373743, 2.5251482916876378],
           [4.776929339068159, 2.795372759575895],
           [3.92033110541304, 2.9018927284871063],
           [2.999998066091118, 2.929924058932193],
           [2.0796652780381826, 2.90189200881968],
           [1.2230677654766597, 2.7953714133566603],
           [0.544928391271399, 2.5251464933327794],
           [0.3027360471605494, 1.875038145804603],
           [0.302736726373967, 1.1249605602741133]]

##    [0.000, 0.000] -> [0.545, 0.475]
##    [1.000, 0.000] -> [1.223, 0.205]
##    [2.000, 0.000] -> [2.080, 0.098]
##    [3.000, 0.000] -> [3.000, 0.070]
##    [4.000, 0.000] -> [3.920, 0.098]
##    [5.000, 0.000] -> [4.777, 0.205]
##    [6.000, 0.000] -> [5.455, 0.475]
##    [6.000, 1.000] -> [5.697, 1.125]
##    [6.000, 2.000] -> [5.697, 1.875]
##    [6.000, 3.000] -> [5.455, 2.525]
##    [5.000, 3.000] -> [4.777, 2.795]
##    [4.000, 3.000] -> [3.920, 2.902]
##    [3.000, 3.000] -> [3.000, 2.930]
##    [2.000, 3.000] -> [2.080, 2.902]
##    [1.000, 3.000] -> [1.223, 2.795]
##    [0.000, 3.000] -> [0.545, 2.525]
##    [0.000, 2.000] -> [0.303, 1.875]
##    [0.000, 1.000] -> [0.303, 1.125]


testpath2 = [[1, 0], # Move in the shape of a plus sign
             [2, 0],
             [2, 1],
             [3, 1],
             [3, 2],
             [2, 2],
             [2, 3],
             [1, 3],
             [1, 2],
             [0, 2], 
             [0, 1],
             [1, 1]]

answer2 = [[1.239080543767428, 0.5047204351187283],
           [1.7609243903912781, 0.5047216452560908],
           [2.0915039821562416, 0.9085017167753027],
           [2.495281862032503, 1.2390825203587184],
           [2.4952805300504783, 1.7609262468826048],
           [2.0915003641706296, 2.0915058211575475],
           [1.7609195135622062, 2.4952837841027695],
           [1.2390757942466555, 2.4952826072236918],
           [0.9084962737918979, 2.091502621431358],
           [0.5047183914625598, 1.7609219230352355],
           [0.504719649257698, 1.2390782835562297],
           [0.9084996902674257, 0.9084987462432871]]

##    [1.000, 0.000] -> [1.239, 0.505]
##    [2.000, 0.000] -> [1.761, 0.505]
##    [2.000, 1.000] -> [2.092, 0.909]
##    [3.000, 1.000] -> [2.495, 1.239]
##    [3.000, 2.000] -> [2.495, 1.761]
##    [2.000, 2.000] -> [2.092, 2.092]
##    [2.000, 3.000] -> [1.761, 2.495]
##    [1.000, 3.000] -> [1.239, 2.495]
##    [1.000, 2.000] -> [0.908, 2.092]
##    [0.000, 2.000] -> [0.505, 1.761]
##    [0.000, 1.000] -> [0.505, 1.239]
##    [1.000, 1.000] -> [0.908, 0.908]

# solution_check(smooth(testpath1), answer1)
