import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

##################### Coding Problem 1 ##########################
## Part a - Solve the ODE with forward Euler
# It will be helpful to define the anonymous function for the right-hand side
P = lambda p: p*(1-p)*(p-1/2)

# Then define tspan and the initial condition.

# Then solve with a for loop!

## Part b - Solve using backward Euler
# The setup is the same, the for loop is different. Remember to define the
# anonymous function which we called "g". 

## Part c - Solve using the midpoint method
# Again, the setup is exactly the same. All that changes is inside the for
# loop. 

## Part d - Solve with RK4
# Okay, things get a little harder here. Continue as you have been doing.
# Setup is the same, for loop is different. Now remember to define:
# k_1 = ....
# k_2 = ...
# k_3 = ...
# k_4 = ...


######################### Coding problem 2 ###################
## Part (a)
# To solve with solve_ivp we need to define an anonymous function. I've
# defined the two ODEs for R'(t) and J'(t) below. You put them together using
# an adapter function. 
a = 1/2
Rprime = lambda R, J: a*R + J
Rprime = lambda R, J: -R - a*J

# odefun = .... # You define the ode function!

# Initial Condition
x0 = np.array([2, 1])

# Then we solve with
# sol = scipy.integrate.solve_ivp(.... ) # You can fill this in

# Then to get the t values we have
# t = sol.t # uncomment
# How about the R and J values? You do that part!


## (b) 
# Once you have the solution, you just need to index the right way to get the
# solutions at the endpoints!

## (c) 
# This gets a little bit trickier. 
# Let's first start by defining our trange:
dt = 0.1
trange = np.arange(0, 20+dt, dt)

# Then, either set it up so that you have 
x = np.zeros([len(trange), 2])
# or do them separately:
R = np.zeros(len(trange))
J = np.zeros(len(trange))

# With either choice you make, you need to then define the initial condition,
# either with 
x[0, :] = x0
# or
R[0] = 2
J[0] = 1

# Then you will need a for loop to do the rest.
for k in range(len(trange)-1):
    # x[k+1] = ....
    # or use
    # R[k+1] = ...
    # and
    # J[k+1] = ...
    break # Remove this when you write your code!

## (d) 
# This is just indexing again, you got it!

## (e) 
# Remember how we use norm: np.linalg.norm


##################### Coding Problem 3 ##########################
# Define the parameters we are going to use:
g = 9.8
L = 11
sigma = 0.12

## Part a
# We now have two ODEs. Define them below as anonymous functions!

# And initial conditions. This is just like Problem 2 above.

## Part b
# Test your anonymous function.


## Part c
# Solve!
