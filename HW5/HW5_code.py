import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize


##################### Coding Problem 1 ##########################
## Part a - Load in the data
# The data is called 'CO2_data.csv'
M = np.genfromtxt('CO2_data.csv', delimiter=',')

# Once you have M defined from CO2_data, uncomment the 
# following code to define t and CO2
t = M[:, 0]
CO2 = M[:, 1]

A1 = t
A2 = CO2

## (b)
# Define the error function that calculates the sum of squared error.
# I've started this for you, but you need to fill it in and uncomment. 

def sumSquaredError(a,b,r):
    # Define the model y
    y = lambda t: a + b*np.exp(r*t)

    # Compute the error using sum-of-squared error
    error = sum(np.abs(y(t) - CO2)**2)
    return error

A3 = sumSquaredError(300,30,0.03)

# Check the error function by defining A3

## (c)
# We need an adapter function to make this work with scipy.optimize.fmin
# Uncomment the line below to use the adapter function
adapter = lambda p: sumSquaredError(p[0], p[1], p[2])

# Once adapter is defined, use fmin
# We use the following guess
guess = np.array([300, 30, 0.03])
A4 = scipy.optimize.fmin(adapter, guess)

## (d)
# Once we have found the optimal parameters, 
# find the error for those optimal parameters
A5 = sumSquaredError(A4[0],A4[1],A4[2])

## (e)
# Now we do the same thing except with max error. 
# Your function looks similar, except use the max error
def maxError(a,b,r):
    y = lambda t: a + b*np.exp(r*t)
    error = np.amax(np.abs(y(t) - CO2))
    return error

adapter = lambda p: maxError(p[0], p[1], p[2])
A7 = scipy.optimize.fmin(adapter, guess,maxiter=2000)
print(A7)
A6 = sumSquaredError(A7[0],A7[1],A7[2])
print(A6)


## (f)
# This error function has more inputs, but it's the same idea.
# Make sure to use sum of squared error!
def sumSquaredError_2(a,b,r,c,d,e):
    # Define the model y
    y = lambda t: a + b*np.exp(r*t) + c*np.sin(d*(t-e))

    # Compute the error using sum-of-squared error
    error = sum(np.abs(y(t) - CO2)**2)
    return error

A8 = sumSquaredError_2(300,30,0.03,-5,4,0)

# And we need to make a new adapter function
# Again, this will have more inputs but will look pretty similar. 
guess = np.append(A4, np.array([-5,4,0]))
adapter = lambda p: sumSquaredError_2(p[0], p[1], p[2], p[3], p[4], p[5])
A9 = scipy.optimize.fmin(adapter, guess,maxiter=2000)

## (h)
# Once we have found the optimal parameters, find the associated error.
A10 = sumSquaredError_2(A9[0],A9[1],A9[2],A9[3],A9[4],A9[5])

######################### Coding problem 2 ###################
## Part (a)
M = np.genfromtxt('salmon_data.csv', delimiter=',')

year = M[:,0] #Assign the 'year' array to the first column of the data
salmon = M[:,1] #Assign the 'salmon' array to the first column of the data

## (b) - Degree-1 polynomial
A11 = np.polyfit(year, salmon,1)

## (c) - Degree-3 polynomial
A12 = np.polyfit(year, salmon,3)

## (d) - Degree-5 polynomial
A13 = np.polyfit(year, salmon,5)

## (e) - compare to exact number of salmon
exact =  752638 # The exact number of salmon
err1 = np.abs(np.polyval(A11,2022)- exact)/exact
err2 = np.abs(np.polyval(A12,2022)- exact)/exact
err3 = np.abs(np.polyval(A13,2022)- exact)/exact

A14 = np.array([err1, err2, err3])

