# This is a template for the coding portion of Homework 3 in AMATH 301, 
# Winter 2023 

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate

############## Problem 1 ################
M = np.genfromtxt('Plutonium.csv', delimiter=',')
t = M[0, :]
P = M[1, :]

## Part a
# Compute h from the t array

## Part b

## Part c

## Part d
# Uncomment the line below to get A4
# A4 = (-3*P[0] + 4*P[1] - P[2])/(2*h)

## Part e

## Part f
# You may want to use a for loop here
# for k in range(1, len(t)-1):
# 	# fill in here

## Part g

## Part h

## Part i

## Part j


############## Problem 2 ################
# You are going to want to define the integrand as an anonymous function.
mu = 85
sigma = 8.3
integrand = lambda x: np.exp(-(x-mu)**2/(2*sigma**2))/np.sqrt(2*np.pi*sigma**2)

# Let's also define the left and right bounds of the integral
left = 110
right = 130

## Part a

## Part b
# To define the h array, we can take 2 to the power of an array.
power = -np.linspace(1, 16, 16)
# Now create h from that array!

## Part c

## Part d

## Part e

## Part f

