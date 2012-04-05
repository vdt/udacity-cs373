#! /usr/bin/env python

q1_probability_heads = 0.6
print "question 1"
print "we have a loaded coin that comes up heads with 0.6 probability."
print "what's the probability that it comes up tails?"
q1_probability_tails = 1 - q1_probability_heads
print q1_probability_tails
print

print "question 2"
print "now we flip is twice.  what is the probability"
print "that it never comes up heads?"
print (q1_probability_tails ** 2)
print

print "question 3"
print "we now add a fair coin (probability of heads ="
print "0.5). We select a coin at random (0.5 chance), flip"
print "it twice and it gives heads twice.  what is the"
print "probability we picked the loaded coin?"
prob_pick_fair = 0.5
prob_pick_load = 1 - prob_pick_fair
prob_fair_heads = 0.5
prob_load_heads = q1_probability_heads
prob_two_heads_given_pick_load = prob_load_heads ** 2
prob_two_heads_given_pick_fair = prob_fair_heads ** 2
prob_two_heads = prob_two_heads_given_pick_load * prob_pick_load\
    + prob_two_heads_given_pick_fair * prob_pick_fair
prob_pick_load_given_two_heads = \
    prob_two_heads_given_pick_load * prob_pick_load / prob_two_heads
print prob_pick_load_given_two_heads
print

print "question 4"
print "a robot lives in the following environment with 4 states:"
print "[[green, green], [red, green]]"
print "initially it does not know anything about its location."
print "what probabilities would you assign to each cell?"
green = "green"
red = "red"
world = [[green, green], [red, green]]
world_size = 0.0
for row in world:
    for cell in row:
        world_size += 1.0
for row in world:
    for cell in row:
        print 1.0/world_size,
    print

