#! /usr/bin/env python

colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

sensor_wrong = 1 - sensor_right

p_still = 1 - p_move

def array_2D_row_count(array_2D):
    return len(array_2D)

def array_2D_column_count(array_2D):
    rows = array_2D_row_count(array_2D)
    if rows == 0:
        return 0
    else:
        return len(array_2D[0])

def create_uniform_distribution(array_2D):
    p = []
    column_count = array_2D_column_count(array_2D)
    row_count = array_2D_row_count(array_2D)
    element_count = row_count * column_count
    for row in range(row_count):
        p.append([1.0 / element_count for i in range(column_count)])
    return p

def array_2D_normalize(array_2D):
    total = array_2D_sum(array_2D)
    for row in range(len(array_2D)):
        for column in range(len(array_2D[row])):
            array_2D[row][column] /= total
    return array_2D

def array_2D_sum(array_2D):
    total = 0
    for row in array_2D:
        for element in row:
            total += element
    return total

def sense(p, measurement):
    q=[]
    for row in range(array_2D_row_count(p)):
        q.append([])
        for column in range(array_2D_column_count(p)):
            updated = 0
            if colors[row][column] == measurement:
                updated = p[row][column] * sensor_right
            else:
                updated = p[row][column] * sensor_wrong
            q[row].append(updated)
    q = array_2D_normalize(q)
    return q

def move(p, U):
    q = []
    row_move = U[0]
    column_move = U[1]
    row_count = array_2D_row_count(p)
    for row in range(row_count):
        column_count = array_2D_column_count(p)
        q.append([])
        for column in range(column_count):
            old_row = (row - row_move) % row_count
            old_column = (column - column_move) % column_count
            s = p_move * p[old_row][old_column]
            s += p_still * p[row][column]
            q[row].append(s)
    return q

def update_p(p, motion, measurement):
    p = move(p, motion)
    p = sense(p, measurement)
    return p

def update_p_all(p, motions, measurements):
    for motion, measurement in zip(motions, measurements):
        p = update_p(p, motion, measurement)
    return p

p = create_uniform_distribution(colors)

p = update_p_all(p, motions, measurements)

show(p)
