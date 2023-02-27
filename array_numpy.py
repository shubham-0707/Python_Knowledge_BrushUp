# Program to make an array using Numpy...

from numpy import *

arr = arange(0, 10, 2)
print(arr)


#shallow copy
arr1 = array([2, 5, 3, 1, 4])
arr2 = arr1.view()

print(arr1)
print(arr2)

print("address: ", id(arr1))
print("address: ", id(arr2))

#deep copy...

arr3 = arr1.copy()
arr1[2] = 8
print(arr1)
print(arr3)

print("address: ", id(arr1))
print("address: ", id(arr2))

