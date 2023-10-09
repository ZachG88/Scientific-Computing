# HW 2 Code

import numpy as np
import math 
# import matplotlib.pyplot as plt

# Problem 1
pyramid = np.zeros(32)
for k in range(1, 33) :
    pyramid[k-1] = (k * (k + 1) * (2 * k + 1)) / 6

A1 = pyramid    

# Problem 2
## Part 1, defining y
#y1
y_1 = 0
for k in range(100000) :
    y_1 += 0.1
    
A2 = y_1

#y2
y_2 = 0
for k in range(100000000) :
    y_2 += 0.1

A3 = y_2

#y3
y_3 = 0
for k in range(100000000) :
    y_3 += 0.25

A4 = y_3
    
#y4
y_4 = 0
for k in range(100000000) :
    y_4 += 0.5

A5 = y_4

## Part 2, defining x
#x1
A6 = np.absolute(10000 - A2)

A7 = np.absolute(A3 - 10000000)

A8 = np.absolute(25000000 - A4)

A9 = np.absolute(A5 - 50000000)


# Problem 3
Fibonacci = np.zeros(200)
Fibonacci[0] = 1
Fibonacci[1] = 1
for k in range(2, 200) :
    if (Fibonacci[k-1] + Fibonacci[k-2] < 1000000) :
        Fibonacci[k] = Fibonacci[k-1] + Fibonacci[k-2]
    else :
        break

A10 = Fibonacci

N = 0
for k in range(0, 200) :
    if (Fibonacci[k] == 0.0) :
        N = k
        break
    
A11 = N - 1


A12 = Fibonacci[:30]

# Problem 4
A13 = np.linspace(-1 * np.pi, np.pi, 100)

Taylor = np.zeros(100)

for k in range(100) :
    temp = 0
    for l in range(4) :
       temp += (((-1)**l)/(math.factorial(2*l))) * (A13[k]**(2*l))  
    Taylor[k] = temp

A14 = Taylor

print(A6)
print(A7)
print(A8)
print(A9)






    
    
    
