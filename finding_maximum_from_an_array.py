#Program to find the maximum from an array without using the inbuilt function....

from numpy import *
import sys

arr = []
n = int(input("Enter size: "))
maxi = -sys.maxsize-1
for i in range(0, n):
    x = int(input("Enter the value: "))
    arr.append(x)
    maxi = max(maxi, x)

print("The maximum number is : ", maxi)