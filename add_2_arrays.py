#Program to add 2 arrays using for loop...

from numpy import *

arr1 = array([1, 3, 2, 5, 4])
print(len(arr1))
print(arr1)
arr2 = array([9,7, 4, 2, 1])
print(arr2)

list1 = []

for i in range(0 , len(arr1)):
    list1.append(arr1[i]+arr2[i])


print("The array3 is: ", array(list1))