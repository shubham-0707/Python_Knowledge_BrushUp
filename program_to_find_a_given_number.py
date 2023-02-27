#program to find a given number...

from array import *

arr = array('i' , [2 , 1, 4 , 3, 6 , 5])
n = int(input("Enter n : "))

for i in arr:
    if(i==n):
        print("Element found")
        break
else:
    print("Element not found")