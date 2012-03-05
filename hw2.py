#! /usr/bin/env python

# question 1
print "measurement update"
print "is sigma-square of gaussian from combining 2 other gaussians"
print "of same variance smaller, larger, same as old variance?"
print "smaller variance, higher information content"

# question 2
print "new variance"
print "say we have a prior gaussian, mu, sigma-square"
print "and a measurement gaussian with same parameters."
print "what will covariance of new gaussian be after multiplying these?"
print "new sigma-square will be half of old sigma-square"

# question 3
print "heavytail gaussian"
print "is it possible to have a heavytail gaussian using"
print " the standard gaussian formula and changing mu and sigma?"
print "no"

# question 4
print "how many dimensions?"
print "object tracked in 2D using kalman filters estimating"
print "position and velocity"
print "how many dimensions in the state vector?"

# question 5
print "state transition matrix"
print "tricky question"
print "in kalman filter program, we had a matrix F"
print "for delta-t = 0.1,"
print " F matrix (state transition matrix), ((1 delta-t)(0 1))"
print " F = ((1 0.1)(0 1))"
print "now fill in F for 2 dimension, assuming state vector is:"
print "((x)(y)(x-dot)(y-dot))?"
print "F ="
print "((1.0, 0.0, 0.1, 0.0),"
print " (0.0, 1.0, 0.0, 0.1),"
print " (0.0, 0.0, 1.0, 0.0),"
print " (0.0, 0.0, 0.0, 1.0))"

# question 6
print "programming exercise"
print "implement kalman filter in 4-dimensions"
print "i'll give you all the code,"
print "set up:"
print "x, state vector, given"
print "u, motion, given"
print "P, initial uncertainty"
print "\tinitialize uncertainty for the x, y coordinate is 0,"
print "\tbut the covariance for the velocities is 1000"
print "\t indicating that we know the position, but not velocity"
print "F, next state function"
print "H, measurement function"
print "\tproject 4 dimensional state space matrix into 2 dimensions"
print "\t because we can only observe first 2 state variables, position"
print "R, measurement uncertainty"
print "\t2x2, 0.1 as main diagonal, measurement noise"
print "I, identity matrix"
print "see hw2-6.py"
