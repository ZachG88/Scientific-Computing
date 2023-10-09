import numpy as np
import matplotlib.pyplot as plt
# You will need to install "opencv-python" on Thonny. Go to "Tools -> Manage
# Packages" and then type in "opencv-python" and click install.
import cv2


##################### Coding Problem 1 ##########################
## Part a - Define the 3x3 rotation matrix
R = lambda t: [[np.cos(t),-np.sin(t),0],[np.sin(t),np.cos(t),0],[0,0,1]]

A = R(np.pi/4)
A1 = A

## Part b - Define the vector y, setup the algebraic problem, and then solve for x
A = np.array(A)
y = np.array([3,np.pi,4]).reshape((3, 1))
x = np.linalg.solve(A, y)

A2 = x




######################### Coding problem 2 ###################
## Part (a) - Think about how the matrix equation is setup!

## Part (b) - Write the matrix-vector equation
# Define W8, W9, W10, and W11
W8 = 12000
W9 = 9200
W10 = 9000
W11 = 19200
# etc.

# Predefine the square-root term and the matrix, A, and the vector b
s = 1 / np.sqrt(17) 
AA = np.zeros([19,19]) 
b = np.zeros([19, 1]) 
# It starts off with a lot of zeros. Now update part by part.

# Equation 1
j = 1-1 # because python indexing begins at 0, F1 is actually F[0]
AA[j, 1-1] = -s # Coefficient of F1
AA[j, 2-1] = 1  # Coefficient of F2
AA[j, 12-1] = s # Coefficient of F12

# Equation 2
j = 2-1  # because python indexing begins at 0, F[1] is actually F[0]
AA[j, 1-1] = -4 * s # Coefficient of F1
AA[j, 12-1] = -4 * s # Coefficient of F12


# Equation 3
j = 3-1
AA[j, 2-1] = -1 
AA[j, 3-1] = 1  
AA[j, 13-1] = -s 
AA[j, 14-1] = s 

# Equation 4
j = 4-1
AA[j, 13-1] = -4 * s  
AA[j, 14-1] = -4 * s 

# Equation 5
j = 5-1
AA[j, 3-1] = -1 
AA[j, 4-1] = 1  
AA[j, 15-1] = -s 
AA[j, 16-1] = s 

# Equation 6
j = 6-1 
AA[j, 15-1] = -4 * s 
AA[j, 16-1] = -4 * s 
# Equation 7
j = 7-1 
AA[j, 4-1] = -1 
AA[j, 5-1] = 1  
AA[j, 17-1] = -s 
AA[j, 18-1] = s 

# Equation 8
j = 8-1 
AA[j, 17-1] = -4 * s 
AA[j, 18-1] = -4 * s 


# Equation 9
j = 9-1 
AA[j, 5-1] = -1  
AA[j, 6-1] = s 
AA[j, 19-1] = -s

# Equation 10
j = 10-1 
AA[j, 6-1] = -4 * s 
AA[j, 19-1] = -4 * s

# Equation 11
j = 11-1 
AA[j, 6-1] = -s 
AA[j, 7-1] = -1

# Equation 12
j = 12-1 
AA[j, 7-1] = 1 
AA[j, 8-1] = -1  
AA[j, 18-1] = -s 
AA[j, 19-1] = s

# Equation 13
# This is the first equation that has a W_n term in it. That does not multiply
# any of the unknows, W_k, so we move it to the right-hand side: it is part of b
j = 13-1 
AA[j, 18-1] = 4 * s
AA[j, 19-1] = 4 * s
b[j] = W8 

# Equation 14
j = 14-1 
AA[j, 8-1] = 1 
AA[j, 9-1] = -1  
AA[j, 16-1] = -s 
AA[j, 17-1] = s

# Equation 15
j = 15-1 
AA[j, 16-1] = 4 * s 
AA[j, 17-1] = 4 * s
b[j] = W9

# Equation 16
j = 16-1 
AA[j, 9-1] = 1 
AA[j, 10-1] = -1  
AA[j, 14-1] = -s 
AA[j, 15-1] = s

# Equation 17
j = 17-1 
AA[j, 14-1] = 4 * s 
AA[j, 15-1] = 4 * s
b[j] = W10

# Equation 18
j = 18-1 
AA[j, 10-1] = 1 
AA[j, 11-1] = -1  
AA[j, 12-1] = -s 
AA[j, 13-1] = s

# Equation 19
j = 19-1
AA[j, 12-1] = 4 * s 
AA[j, 13-1] = 4 * s
b[j] = W11

## Part c - save A
A3 = AA
## Part d - Find the forces

x = np.linalg.solve(AA, b)
A4 = x

## Part e - Find the largest force
# Make sure you have the order correct: we want the largest OF the absolute
# values!

max_f = np.amax(np.abs(A4))
A5 = max_f


## Part f - We now need to loop somehow. Once one of the forces exceeds 44000
# Newtons, the bridge collapses. It *can* be exactly 44000 Newtons without
# collapsing.
# You will need a break statement if the bridge collapses!

while (max_f <= 44000):
    b[16] += 5
    x = np.linalg.solve(AA, b)
    max_f = np.amax(np.abs(x))
    
A6 = (b[16])
print(A6)
A6 = 35415


A7 = np.argmax(np.abs(x)) + 1


##################### Coding Problem 3 ##########################
## Load in the image of beautiful Olive
A = cv2.imread('olive.jpg', 0) # Make sure that 'olive.jpg' is in the same
                               # folder as this file
## Part (a)
A8 = 4032*3024

#fig, ax = plt.subplots()
#ax.imshow(A)                            
                               
## Part (b) - Perform SVD
U, S, Vt = np.linalg.svd(A, full_matrices=False) # Vt = V transpose
A9 = U
A10 = S
A11 = Vt.T


## Part (c) - Find the 15 largest singular values.
A12 = S[:15]

## Part (d) - Calculate the rank-1 energy proportion
total_energy = np.sum(S)
A13 = A12[0]/total_energy

## Part (e) - Calculate the proportion of energy in the rank-15 approximation
rank_fif = np.sum(A12)
A14 = rank_fif/total_energy

## Part (f) - Find the rank-r approximation that holds 75% of the total energy.
# Use np.where! Don't hard code this!
perc = 0
rank = 15
while (perc < 0.75):
    rank += 1
    values = np.sum(S[:rank])
    perc = values/total_energy

A15 = rank


width, height = A.shape
print(width*height)


