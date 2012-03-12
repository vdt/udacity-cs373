#! /usr/bin/env python

# 1. empty cell
print "what is the probability that zero particles are in stat A?"
print "4 states, N uniform particles"
print "when N = 1, 4, 10?"
def pN(N):
    return 3./4.**N
print pN(1), pN(4), pN(10)

# 2. motion question
print "consider 4 states, [[a b],[c d]].  motion step"
print "50% = p(move horizontally), 50% = p(vertically), 0% diagonal"
print "never stays in same cell"
print "after 1 step, how many do we expect in each cell,"
print "given we start with [[5 3] [3 1]]?"
print "also what do we expect after infinite steps?"
print "A = .5 * 3 + .5 * 3 = ", .5 * 3 + .5 * 3
print "B = .5 * 5 + .5 * 1 = ", .5 * 5 + .5 * 1
print "C = .5 * 1 + .5 * 5 = ", .5 * 1 + .5 * 5
print "D = .5 * 3 + .5 * 5 = ", .5 * 3 + .5 * 3

print "3. single particle"
print "particle filter with N=1 particle.  what happens?"
print "works fine"
print "ignores robot measurements"
print "ignores robot motion"
print "it likely fails"
print "none of the above"
