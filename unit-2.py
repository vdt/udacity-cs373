#! /usr/bin/env python

# Write a program that will iteratively update and
# predict based on the location measurements 
# and inferred motions shown below. 

def update(mean1, var1, mean2, var2):
    new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1/(1/var1 + 1/var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0
sig = 10000

#Please print out ONLY the final values of the mean
#and the variance in a list [mu, sig]. 

# Insert code here
def step(mu, sig, measurement, motion):
    mu, sig, measurement, motion =\
        [float(mu), float(sig), float(measurement), float(motion)]
    mu, sig = update(mu, sig, measurement, measurement_sig)
    mu, sig = predict(mu, sig, motion, motion_sig)
    return [mu, sig]

def all_steps(mu, sig, measurements, motions):
    for measurement, motion in zip(measurements, motions):
        mu, sig = step(mu, sig, measurement, motion)
    return [mu, sig]

mu, sig = all_steps(mu, sig, measurements, motion)

print [mu, sig]
