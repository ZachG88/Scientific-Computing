# Import necessary packages for homework
import numpy as np
#import matplotlib.pyplot as plt

## Problem 1
# Part a
x = 3.1
A1 = x

# Part b
y = -29
A2 = y

# Part c - "e" is implemented in numpy with 
z = 9*np.e
A3 = z

# Part d
# There are two ways to do this. We can raise the number "e" to the 4th power,
# or (preferably) we can use np.exp() which takes e to a power.
w = np.exp(4)
A4 = w
# print(A4) # uncomment this line to check your work!

# Part e
A5 = np.sin(np.pi)

## Problem 2
x = np.linspace(0, 1, 5)
x = np.pi * x
x = np.cos(x)
A6 = x

## Problem 3
# Part a
u = np.linspace(3, 4, 6)
A7 = u

print(A7)

# Part b
v = np.arange(0, 4.5 , .75)
A8 = v

# Part c
w = v + 2 * u
A9 = w

# Part d
w = u ** 3
A10 = w

# Part e
x = np.tan(u) + np.exp(v)
A11 = x

# Part f
A12 = u[2]
print(A12)

## Problem 4
# Part a
z = np.arange(-6, 3.01, .01)
A13 = z

# Part b
A14 = z[0::2]

# Part c
A15 = z[0::3]

# Part d
A16 = z[-5:]

