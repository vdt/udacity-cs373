#! /usr/bin/env python

# Write a program to update your mean and variance
# when given the mean and variance of your belief
# and the mean and variance of your measurement.
# This program will update the parameters of your
# belief function.

def sigma_prime(mu, sigma_square, nu, r_square):
    return (r_square * mu + sigma_square * nu)/(sigma_square + r_square)

def sigma_square_prime(sigma_square, r_square):
    return 1./(1./sigma_square + 1./r_square)

def update(mean1, var1, mean2, var2):
    new_mean = sigma_prime(mean1, var1, mean2, var2)
    new_var = sigma_square_prime(var1, var2)
    return [new_mean, new_var]

print update(10.,8.,13., 2.)
