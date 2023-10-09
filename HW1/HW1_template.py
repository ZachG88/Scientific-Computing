# This is a template that you can and should use for your Homework 1 solutions
# for AMATH 301. Some parts are completed for you and you will need to fill in
# others. 

# We always start with importing the modules we will need for this assignment.
# The only two modules we have talked about so far are numpy and matplotlib.
import numpy as np
import matplotlib.pyplot as plt

## Problem 1
# Part a
x = 3.1
A1 = x

# Part b
y = -29
A2 = y

# Part c - "e" is implemented in numpy with np.e
z = 9*np.e
A3 = z

# Part d
# There are two ways to do this. We can raise the number "e" to the 4th power,
# or (preferably) we can use np.exp() which takes e to a power.
w = np.exp(4)
A4 = w
# print(A4) # uncomment this line to check your work!

# Part e
# You have to do this one! Don't do any simplifications, just write the code
# and let python do the computation for you. 


## Problem 2
# I'll start you off with:
x = np.linspace(0, 1, 5) # First create the vector [0, 1/4, 2/4, 3/4, 4/4]
# Now once that is created, we can just multiply by pi
x = np.pi*x # Notice that I rewrite over x because I don't need the old
            # definition of x anymore.
# Note what I have done. I could just create the vector [0, 1/4, 2/4, 3/4, 4/4]
# by typing it in, but why do that when there is built-in functions! The way I
# have done it here is the programatic way to create this vector. You should do
# that when you can. 

# Now that you have x, how can you create A6? That's up to you.


## Problem 3
# Try to do this problem like I've setup the last problem: do not type in u or
# v directly, instead use built-in functions, linspace and arange. 
# I've given you an example on how to use linspace above. Use that to create
# either u or v (hint: which one is defined by the number of points?
# You have seen how linspace works. Look up "numpy arange" on google to see how
# arange works.

## Problem 4
# Again try to do this problem without "hardcoding." That means that you should
# use built-in functions when you can. Use *indexing* instead
# of typing in the answer directly. 

# Assuming that you have z defined correctly, the following code will give you
# A14. Uncomment it and check!
# temp = np.arange(0, len(z), 2) # This creates an array from 0 to the length
                                 # of z with a spacing of 2 (every other)
# A14 = z[temp] # Now we can use this array to index, giving what we want!
# print(A14) # Uncomment this line to check your work!

# I'll show you one more way to do this. 
# A14 = z[0::2] # This says take elements of z starting at 0, up through the
                # end, in spacing of 2s
                # We could also get rid of the zero, having just z[::2], check
                # for yourself!

