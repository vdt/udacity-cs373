#! /usr/bin/env python

# 1 probability
print "if p(x) = 2, p(!x) = ?"
p_x = 0.2
p_not_x = (1 - 0.2)
print "p(!x) = %f" % p_not_x
print
print "if p(x) = 0.2, p(y) = 0.2, x and y independent, p(x,y) = ?"
p_x = 0.2
p_y = 0.2
p_x_and_y = p_x * p_y
print "p(x,y) = %f" % p_x_and_y
print
print "p(x) = 0.2, p(y|x) = 0.6, p(y|!x) = 0.6, p(y) = ?"
p_x = 0.2
p_y_given_x = 0.6
p_y_given_not_x = 0.6
p_not_x = 1 - p_x
p_y = p_y_given_x * p_x + p_y_given_not_x * p_not_x
print "p(y) = %f" % p_y
print

# 2 localization

print "i honestly don't understand the question."
print "i think the answer is exponentially. since that's how much"
print "state space increases with new dimensions of roughly the same size."

# 3 bayes rule

p_fire = 0.001
p_not_fire = (1 - p_fire)
p_lie = 0.1
p_truth = (1 - p_lie)

# neighbor says it burns
# what is non-normalized probability of fire given neighbor says burning
# p_bar(F|B) = p(B|F)*P(F)
p_burning_given_fire = p_truth
p_bar_fire_given_burning = p_burning_given_fire * p_fire
print "non-normalized probability of fire given neighbor says fire"
print p_bar_fire_given_burning

# what is non-normalized probability of not fire given neighbor says burning
p_burning_given_not_fire = p_lie
p_bar_not_fire_given_burning = p_burning_given_not_fire * p_not_fire
print "non-normalized p of !fire given neighbor says burning"
print p_bar_not_fire_given_burning

normalizer = p_bar_fire_given_burning + p_bar_not_fire_given_burning

# what is the normalized p of fire given burning
p_fire_given_burning = p_bar_fire_given_burning / normalizer
print "normalized p of fire given burn"
print p_fire_given_burning

# what is the normalized p of not fire given burn
p_not_fire_given_burning = p_bar_not_fire_given_burning / normalizer
print "normalized p of not fire given b"
print p_not_fire_given_burning
