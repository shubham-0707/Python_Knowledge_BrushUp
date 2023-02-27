# Taking user input in array...

from array import *

arr = array('i' ,[])

n = int(input("Enter the size of the array: "))

for i in range(n):
    val = int(input("Enter the value: "))
    arr.append(val)

print(arr)

search = int(input("Enter the search element : "))

k = 0

for a in arr:
    if(search==a):
        print("Element found !")
        print(k)
        break
    k+=1


print(arr.index(search))