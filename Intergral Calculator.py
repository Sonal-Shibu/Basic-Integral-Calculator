import numpy as np
import math

xMin=1.0 #Lower bound/limit
xMax=3.0 #Higher bound/limit
dx=1e-5 #this is dx value make it small as you want but the smaller it is the.... 
#......more computing time you need, 1e-4 should be small enough for moost of the applications

x=np.arange(xMin,xMax,dx) # we are discretizing between the lower and higher bound with dx between the spaces
f_int=np.zeros(len(x)) # if alot programing languages it is important to specify the size of the array first. So this is the final solutin array. 

for i in range(0,len(x)): #In maths we have to use an iterate apporach to solve integrals, here it is the same! But in here it is a for loop. 
#...i is the counting variable which looks at the elements
    f_int[i]=x[i]**2 * math.exp(-x[i])*math.sin(x[i])*dx # f(x)=x^2 * e^-x * sin(x), this is the mathmatical function

print("The area underneith of the function is: " ,sum(f_int))