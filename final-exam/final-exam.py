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

print "question 7"
print 'it now senses "red" again.  update your probabilities.'
p = moved_north_world
for row_index in range(len(world)):
    for column_index in range(len(world)):
        if world[row_index][column_index] == red:
            p[row_index][column_index] *= 0.8
        else:
            p[row_index][column_index] *= 0.2
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

print "question 8"
print "Q3:1-d kalman filter"
print "compute, for the following two Gaussians, the result of applying bayes"
print "rule. Think of gaussian 1 as the prior, and gaussian 2 as the"
print "measurement probability."
print "gaussian 1, guassian 2, result"
print "mu sigma^2, mu sigma^2, mu sigma^2"
def mu_prime(mu, sigma_square, nu, r_square):
    return (r_square * mu + sigma_square * nu)/(sigma_square + r_square)

def sigma_square_prime(sigma_square, r_square):
    return 1./(1./sigma_square + 1./r_square)

def sigma_mu_update(mean1, var1, mean2, var2):
    new_mean = mu_prime(mean1, var1, mean2, var2)
    new_var = sigma_square_prime(var1, var2)
    return [new_mean, new_var]
print sigma_mu_update(1., 1., 1., 1.)
print "question 9"
print sigma_mu_update(1., 1., 5., 1.)
print "question 10"
print sigma_mu_update(1., 1., 5., 4.)
print

print "question 11"
print "exactly the same question as before, but replacing"
print "measurement step with a motion step."
def kalman_predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]
print kalman_predict(1., 1., 1., 1.)
print "q12"
print kalman_predict(1., 1., 5., 1.)
print "q13"
print kalman_predict(1., 1., 5., 4.)
print

print "q5: particle filters"
print "q14"
print "a robot lives in the following non-cyclic environment"
print "with 4 states"
print "[[green, green], [red, green]]"
print "challenge"
print "in global localization, suppose we have 12"
print "particles.  what is the probability that all cells have at"
print "least one particle, for the initial uniform sample?"
prob_1_empty = ((3./4.)**12.)*4.
prob_2_empty = ((2./4.)**12.)*4.
prob_3_empty = ((1./4.)**12.)*4.
prob_4_empty = 0.
prob_0_empty = 1 - prob_1_empty - prob_2_empty - prob_3_empty - prob_4_empty
print "prob_0_empty = ", prob_0_empty
print "q15"
print "assume each cell has exactly 3.  what is the normalized"
print 'sum of all the weights in each cell, if we observe "red"'
print "and assume a 0.2 measurement error probability?"
red = "red"
green = "green"
world = [[green, green], [red, green]]
measurement_error = 0.2
measurement_correct = 1 - measurement_error
measurement = red
world_size = 0.0
for row in world:
    for cell in row:
        world_size += 1
p = [[measurement_error/world_size if cell != measurement \
          else measurement_correct/world_size for cell in row] for row in world]
p_sum = 0.0
for row in p:
    for cell in row:
        p_sum += cell
p_normalized = [[cell/p_sum for cell in row] for row in p]
for row in p_normalized:
    for cell in row:
        print "%0.03f" % cell,
    print
print
print "q16"
print "assume each cell has 3 particles.  the robot moves north,"
print "but the world is not cyclic (so if the robot hits a wall, it"
print "just won't move).  what is the number of particles in each"
print "cell after motion? assume we use each particle once,"
print "ignore resampling, and assume motion is noise-free"
print [[6, 6], [0, 0]]
print

print "q6: a* planning (challenge)"
print "q17"
print "for the following planning problem, there are nodes that A* must expand"
print "and other nodes A* will never expand (assuming the heuristic is"
print "admissible).  assume only up/down/left/right expansion, no diagonal"
print "motion."
world = []
world_row_count = 4
world_column_count = 4
for row in range(world_row_count):
    world.append([])
    for column in range(world_column_count):
        world[row].append(' ')
world[0][0] = 's'
world[3][3] = 'g'
for row in world:
    print row
print "must expand:"
must_expand = [[cell for cell in row] for row in world]
for row in range(4):
    must_expand[row][0] = '*'
for column in range(4):
    must_expand[3][column] = '*'
for row in must_expand:
    print row
print "q18"
print "never expand"
never_expand = [[cell for cell in row] for row in world]
for row in range(2):
    for column in range(2, 4):
        never_expand[row][column] = '*'
never_expand[2][3] = '*'
for row in never_expand:
    print row
print

print "q7: PID Control"
print "(q19 in the sidebar)"
print "Say you are having difficulties keeping a car on a circular"
print "reference trajectory.  what modification could make it easier to"
print "stay near the reference trajectory?"
print "_ increase length of car"
print "* decrease length of car"
print "* increase maximum steering angle"
print "_ increase speed of the car"
print "_ remove p term from your controller"
print "* increase the diameter of the circle"
print "_ none of the above"
