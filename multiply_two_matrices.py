# Program to multiply two matrices...

from numpy import *

m1 = matrix('1 , 2 , 3; 6 , 5 , 4 ; 7 , 8 , 9')
m2 = matrix('4 , 3 , 2 ; 1 , 2, 3; 6 , 8, 7')

print("Matrix 1: ", m1)
print("Matrix 2: ", m2)

m3 = m1*m2
print("Product of two matrices: ", m3)