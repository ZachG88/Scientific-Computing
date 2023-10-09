import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

##################### Coding Problem 1 ##########################
## Part a - Solve the ODE with forward Euler
# It will be helpful to define the anonymous function for the right-hand side
P = lambda p: p*(1-p)*(p-1/2)

# Then define tspan and the initial condition.
tspan = np.arange(0, 10 + 0.5, 0.5)
f = np.zeros(len(tspan))
dt = 0.5
f[0] = 0.9

# Then solve with a for loop!
for k in range(len(f) - 1):
        f[k + 1] = f[k] + dt * P(f[k]) # Forward Euler step
A1 = f
## Part b - Solve using backward Euler
# The setup is the same, the for loop is different. Remember to define the
# anonymous function which we called "g".
tspan = np.arange(0, 10 + 0.5, 0.5)
b = np.zeros(len(tspan))
dt = 0.5
b[0] = 0.9

for k in range(len(b) - 1):
    g = lambda z: z - b[k] - dt * P(z)
     # Forward Euler step
    b[k+1] = scipy.optimize.fsolve(g, b[k])
A2 = b

## Part c - Solve using the midpoint method
# Again, the setup is exactly the same. All that changes is inside the for
# loop.
tspan = np.arange(0, 10 + 0.5, 0.5)
m = np.zeros(len(tspan))
dt = 0.5
m[0] = 0.9

for k in range(len(m) - 1):
    k1 = P(m[k])
    k2 = P(m[k] + (dt/2)*k1)
    m[k + 1] = m[k] + dt * k2
A3 = m

## Part d - Solve with RK4
# Okay, things get a little harder here. Continue as you have been doing.
# Setup is the same, for loop is different. Now remember to define:
tspan = np.arange(0, 10 + 0.5, 0.5)
r = np.zeros(len(tspan))
dt = 0.5
r[0] = 0.9

for k in range(len(r) - 1):
    k1 = P(r[k])
    k2 = P(r[k] + (dt/2)*k1)
    k3 = P(r[k] + (dt/2)*k2)
    k4 = P(r[k] + dt*k3)
    r[k+1] = r[k] + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)
A4 = r


######################### Coding problem 2 ###################
## Part (a)
# To solve with solve_ivp we need to define an anonymous function. I've
# defined the two ODEs for R'(t) and J'(t) below. You put them together using
# an adapter function. 
a = 1/2
Rprime = lambda R, J: a*R + J
Jprime = lambda R, J: -R - a*J

odefun = lambda t, v: np.array([Rprime(v[0],v[1]), Jprime(v[0],v[1])])# You define the ode function!

# Initial Condition
x0 = np.array([2, 1])

# Then we solve with
sol = scipy.integrate.solve_ivp(odefun, [0, 20], x0)

# Then to get the t values we have
t = sol.t # uncomment
vsol = sol.y
R = vsol[0, :]
J = vsol[1, :]

A5 = R
A6 = J

## (b) 
# Once you have the solution, you just need to index the right way to get the
# solutions at the endpoints!
A7 = [A5[-1], A6[-1]]



## (c) 
# This gets a little bit trickier. 
# Let's first start by defining our trange:
dt = 0.1
trange = np.arange(0, 20+dt, dt)

# Then, either set it up so that you have 
# or do them separately:
R = np.zeros(len(trange))
J = np.zeros(len(trange))

R[0] = 2
J[0] = 1

# Then you will need a for loop to do the rest.
for k in range(len(trange)-1):
    R[k+1] = R[k] + dt*Rprime(R[k], J[k])
    J[k+1] = J[k] + dt*Jprime(R[k], J[k])
    #break # Remove this when you write your code!
A8 = R
A9 = J

## (d) 
# This is just indexing again, you got it!
A10 = [A8[-1], A9[-1]]



## (e) 
# Remember how we use norm: np.linalg.norm
diff = np.subtract(A10,A7)
A11 = np.linalg.norm(diff)


##################### Coding Problem 3 ##########################
# Define the parameters we are going to use:
g = 9.8
L = 11
sigma = 0.12

## Part a
# We now have two ODEs. Define them below as anonymous functions!
theta_prime = lambda t, y: y[1]
v_prime = lambda t, y: -1*(g/L)*np.sin(y[0]) - sigma*y[1]
# And initial conditions. This is just like Problem 2 above.
y0 =[-np.pi/8, -0.1]

## Part b
# Test your anonymous function.
odefun = lambda t, y: [y[1], -1*(g/L)*np.sin(y[0]) - sigma*y[1]]
p = np.array([2,3])
A12 = odefun(1,p)

## Part c
# Solve!
sol = scipy.integrate.solve_ivp(odefun, [0, 50], y0)
t = sol.t # uncomment
vsol = sol.y
A13 = vsol