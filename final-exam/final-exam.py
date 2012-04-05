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
p = [[1.0 / world_size for cell in row] for row in world]
for row in p:
    for cell in row:
        print "%0.03f" % cell,
    print
print

print "question 5"
print 'now the robot senses "red" but has a measurement'
print "error probability of 0.2. Update your probabilities."
p = [[0.8 if cell == red else 0.2 for cell in row] for row in world]
p_sum = 0.0
for row in p:
    for cell in row:
        p_sum += cell
p = [[cell/p_sum for cell in row] for row in p]
for row in p:
    for cell in row:
        print "%0.03f" % cell,
    print
print

print "question 6"
print "it now moves north by one step (the world is not cyclic -"
print "so if the robot hits a wall, it just won't move). update"
print "your probabilities."
moved_north_world = [[p[0][0] + p[1][0], p[0][1] + p[1][1]], [0, 0]]
for row in moved_north_world:
    for cell in row:
        print "%0.03f" % cell,
    print
print
