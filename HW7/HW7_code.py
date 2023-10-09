import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
import scipy.integrate
import time


##################### Coding Problem 1 ##########################
## Part a - Solve with Adam's Moulton method
# Define the ODE and root-finding problem
dydt = lambda t, y: (5e5)*(-y+np.sin(t))
tspan = np.linspace(0, 2*np.pi, 100)
dt = tspan[1]
y = np.zeros(len(tspan))
y0 = 0
y[0] = y0

g = lambda z: z - y[0] - dt/2 * dydt(tspan[1], z)

A1 = g(3)


## Part b - Implement Adam's Moulton
# Then define tspan and the initial condition.

# Then solve with a for loop!
for k in range(len(y) - 1):
    g = lambda z: z - y[k] - dt/2 * dydt(tspan[k+1], z)
    y[k+1] = scipy.optimize.fsolve(g, y[k])
    
A2 = y


######################### Coding problem 2 ###################
## Part (a) - setup ODE
# To solve you are going to need the ODEs for y1, y2, and y3. 
# First define the constants
s = 77.27
w = 0.161
q = 1

y1_prime = lambda y1, y2, y3: s*(y2 - y1*y2 + y1 - q*y1**2)
y2_prime = lambda y1, y2, y3: (1/s)*(-y2-y1*y2+y3)
y3_prime = lambda y1, y2, y3: w*(y1-y3)

odefun = lambda t, y: [y1_prime(*y), y2_prime(*y), y3_prime(*y)]

arr = [2,3,4]

A3 = odefun(1, arr)
## (b) Solve for 10 logarithmically spaced points, using RK45
qs = np.logspace(0, -5, 10)

A4 = np.zeros([3, 10])

for k in range(len(qs)):
    q = qs[k]
    sol = scipy.integrate.solve_ivp(odefun, [0, 30], [1,2,3])
    arr = sol.y[:,-1]
    for l in range(3) :
      A4[l,k] =  arr[l]


## (c)  Solve for 10 logarithmically spaced points, using BDF
A5 = np.zeros([3, 10])

for k in range(len(qs)):
    q = qs[k]
    sol = scipy.integrate.solve_ivp(odefun, 
                            [0, 30],
                            [1,2,3], method='BDF')
    arr = sol.y[:,-1]
    print(arr)
    for l in range(3) :
      A5[l,k] =  arr[l]
print(A4)

##################### Coding Problem 3 ##########################
# Define the parameters we are going to use:
mu = 200

## Part a - define the ODEs
dxdt = lambda t, init: init[1]
dydt = lambda t, init: mu*(1-init[0]**2)*init[1]-init[0]

init = [2,3]

A6 = dxdt(1, init)
A7 = dydt(1, init)

## Part b
# Solve using BDF. What are the initial conditions?
odefun = lambda t, init: [dxdt(t, init), dydt(t, init)]
x0 = 2
y0 = 0
tspan = (0.0, 400.0)

sol = scipy.integrate.solve_ivp(fun=odefun, t_span=tspan, y0=[x0, y0], method='RK45')
A8 = sol.y[0]

## Part c
sol2 = scipy.integrate.solve_ivp(fun=odefun, t_span=tspan, y0=[x0, y0], method='BDF')
A9 = sol2.y[0]

## Part d
A10 = len(A8)/len(A9)

## Part e - linearized version
dxdt = lambda t, init: init[1]
dydt = lambda t, init: mu*init[1]-init[0]

init = [2,3]

A11 = dxdt(1, init)
A12 = dydt(1, init)


## Part f - linear system
# Example:
A = np.array([[0, 1], [-1, mu]])
A13 = A

## Part g
dt = 0.01

## Part h

A14 = 0

## Part i 
I = np.eye(2)
C = I - dt*A

tspan = np.arange(0, 400 + dt, dt)
b = np.zeros([len(tspan), 2])
b[0, ] = [0,0]

for k in range(len(b) - 1):
    b[k+1, ] = np.linalg.solve(C, odefun(tspan[k], b[k]))
    
A16 = b[:, 0]

A15 = C

print(A16)


