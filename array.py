#This program is to check the implementation of array in python...

from array import *

vals  = array('i' , [5 , 2 , 1 , 3 , 4])

print("Vals: ")
for i in vals:
    print(i)

vals.reverse()

print("newArr: ")
newArr = array(vals.typecode , (a for a in vals))
for i in newArr:
    print(i)