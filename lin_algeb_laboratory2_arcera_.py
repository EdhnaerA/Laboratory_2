# -*- coding: utf-8 -*-
"""Lin-Algeb_Laboratory2_Arcera_.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fuAhh0evZgwhW0_mhy2I_LpE4f5OyiYU

# Laboratory no.2 Introduction of Vectors
"""

import numpy as np

A = np.array([3, 3, -3])
B = np.array([-5, -2, 0])
C = np.array([2, -3, 5])
D = np.array([4, -3, 2])
E = np.array([5, -1, 4])

"""### Addition and Subtraction

"""

R = A + B + C - D - E #Eager Execution
print(' VECTORS ', R)

R1 = np.add(A,B) #Functional Method
R2 = np.subtract(R1,C)
R3 = np.add(R2,D)
R4 = np.subtract(R3,E)
print ("VECTORS", R4)

"""### Multiplication and Division"""

R = A * C / E
print('VECTORS ', R)

R1 = np.multiply(B,D)
R2 = np.divide(R1,E)
print ("VECTORS",R2)

"""### Squaring and Square root"""

X = np.array([4,9,25])
Y = np.array([2,3,5])

R1 = np.sqrt(np.square(X))
print ("VECTORS",R1)

"""### Summation"""

arr = [30, -9, .3, 5, 2]   
   
print("SUM OF ARRAY : ", np.sum(arr))  
   
print("SUM OF ARRAY(uint8) : ", np.sum(arr, dtype = np.uint8))  
print("SUM OF ARRAY(float32) : ", np.sum(arr, dtype = np.float32))

# 2D array  
arr = [[16, 18, 24, 23,34],    
       [35, 26, 17, 10, 23],   
       [13, 21, 14, 18, 3,]]   
   
print("\nSUM OF ARRAY : ", np.sum(arr))  
   
print("SUM OF ARRAY(uint8) : ", np.sum(arr, dtype = np.uint8))  
print("SUM OF ARRAY(float32) : ", np.sum(arr, dtype = np.float32))

"""### Visualizing the vectors"""

import matplotlib.pyplot as plt

a = [3.0,5.0]
b = [6.0,7.0]

head_length = 0.7

dx = b[0] - a[0]
dy = b[1] - a[1]

vec_ab = [dx,dy]

vec_ab_magnitude = np.sqrt(dx**2+dy**2)

dx = dx / vec_ab_magnitude
dy = dy / vec_ab_magnitude

vec_ab_magnitude = vec_ab_magnitude - head_length

ax = plt.axes()

ax.arrow(a[0], a[1], vec_ab_magnitude*dx, vec_ab_magnitude*dy, head_width=0.5, head_length=0.7, fc='lightblue', ec='black')

plt.scatter(a[0],a[1],color='black')
plt.scatter(b[0],b[1],color='black')

ax.annotate('A', (a[0]-0.4,a[1]),fontsize=14)
ax.annotate('B', (b[0]+0.3,b[1]),fontsize=14)

plt.grid()

plt.xlim(0,10)
plt.ylim(0,10)

plt.title('Vizualing the vectors',fontsize=10)