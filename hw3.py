#! /usr/bin/env python

# 1. empty cell
print "what is the probability that zero particles are in stat A?"
print "4 states, N uniform particles"
print "when N = 1, 4, 10?"
def pN(N):
    return 3./4.**N
print pN(1), pN(4), pN(10)
