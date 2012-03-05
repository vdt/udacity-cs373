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
print "x, state vector"
print "u, motion"
print "P"
print "F"
print "H"
print "R"
print "I"
