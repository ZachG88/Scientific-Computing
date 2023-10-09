# Code for HW 3, Zach Gendreau

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate

############## Problem 1 ################
M = np.genfromtxt('Plutonium.csv', delimiter=',')
t = M[0, :]
P = M[1, :]

## Part a
# Compute h from the t array
h = t[1] - t[0]
A1 = h

## Part b
deriv_1 = (P[int(0+A1)] - P[0])/A1
A2 = deriv_1

## Part c
deriv_2 = (P[40]-P[int(40-A1)])/A1
A3 = deriv_2

## Part d
# Uncomment the line below to get A4
A4 = (-3*P[0] + 4*P[1] - P[2])/(2*h)

## Part e
A5 = (-3*P[40] + 4*P[39] - 1*P[38])/ (-2*h)

## Part f
# You may want to use a for loop here
differences = np.zeros(41)
differences[0] = A4
differences[40] = A5

for k in range(1, len(t)-1):
    differences[k] = (P[int(k+h)] - P[int(k-h)])/2*h
A6 = differences

## Part g
#decay = np.zeros(41)
#for k in range(0, len(t)):
#    decay[k] = ((P[k]**-1)*(A6[k]))
A7 = (-1*A6)/P


## Part h
A8 = np.mean(A7)


## Part i
A9 = (np.log(2))/A8

## Part j
A10 = (P[21] - 2*P[22] + P[23])/(h**2)



############## Problem 2 ################
# You are going to want to define the integrand as an anonymous function.
mu = 85
sigma = 8.3
integrand = lambda x: np.exp(-(x-mu)**2/(2*sigma**2))/np.sqrt(2*np.pi*sigma**2)

# Let's also define the left and right bounds of the integral
left = 110
right = 130

## Part a
output = scipy.integrate.quad(integrand, left, right)
A11 = output[0]

## Part b
# To define the h array, we can take 2 to the power of an array.
power = -np.linspace(1, 16, 16)
# Now create h from that array!
h = 2**power

left_rule = np.zeros(16)
for k in range(0, len(h)):
    step = h[k]
    x_vals = np.arange(110, 130+step, step)
    approx = np.zeros(len(x_vals) + 1)
    for l in range(0, len(x_vals)):
        approx[l] = (integrand(x_vals[l])) * step
    left_rule[k] = sum(approx)
A12 = left_rule

## Part c
right_rule = np.zeros(16)
for k in range(0, len(h)):
    step = h[k]
    x_vals = np.arange(110, 130+step, step)
    approx = np.zeros(len(x_vals) + 1)
    for l in range(0, len(x_vals)):
        approx[l] = (integrand(x_vals[l]+step)) * step
    right_rule[k] = sum(approx)
A13 = right_rule


## Part d
mid_rule = np.zeros(16)
for k in range(0, len(h)):
    step = h[k]
    x_vals = np.arange(110, 130+step, step)
    approx = np.zeros(len(x_vals) + 1)
    for l in range(0, len(x_vals)):
        approx[l] = (integrand(x_vals[l] + (.5*step))) * step
    mid_rule[k] = sum(approx)
A14 = mid_rule


## Part e
trap_rule = np.zeros(16)
for k in range(0, len(h)):
    step = h[k]
    x_vals = np.arange(110, 130+step, step)
    approx = np.zeros(len(x_vals) + 1)
    for l in range(0, len(x_vals)):
        approx[l] = ((integrand(x_vals[l]) + integrand(x_vals[l]+step)) / 2) * step
    trap_rule[k] = sum(approx)
A15 = trap_rule


## Part f
simp_rule = np.zeros(16)
for k in range(0, len(h)):
    step = h[k]
    x_vals = np.arange(110, 130+step, step)
    odd_approx = 0
    for l in range(1, len(x_vals)-1, 2):
        odd_approx += integrand(x_vals[l])
    even_approx = 0
    for l in range(2, len(x_vals)-2, 2):
        even_approx += integrand(x_vals[l])
    
    tot_sum = (step/3) * (integrand(110) + integrand(130) + 4*(odd_approx) + 2*(even_approx))
    simp_rule[k] = tot_sum
A16 = simp_rule

exact = A11
abs_left = abs(exact - left_rule)

abs_right = abs(exact - right_rule)

abs_mid = abs(exact - mid_rule)

abs_trap = abs(exact - trap_rule)

abs_simp = abs(exact - simp_rule)

plt.figure()
plt.loglog(abs_left,error[:, 0], 'bo',linewidth = 2,marker = "o")
#plt.plot(t,abs_right,color = "orange",linewidth = 2,marker = "o")
#plt.plot(t,abs_mid,color = "yellow",linewidth = 2,marker = "o")
#plt.plot(t,abs_trap,color = "green",linewidth = 2,marker = "o")
#plt.plot(t,abs_simp,color = "blue",linewidth = 2,marker = "o")
plt.show()




