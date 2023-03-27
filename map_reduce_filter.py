#This program is made to demonstrate the function of Map Reduce and Filter...

from functools import reduce

lst = [2, 1, 4, 6, 2, 7, 4]

#To get all the even from the list..

evens = list(filter(lambda a:a%2==0, lst))
print(evens)

#To perform operations on all the elements...

doubles = list(map(lambda a:a*2, evens))

print(doubles)

#To perform the reduce operation..

sum_all = reduce(lambda a, b: a+b, doubles)
print(sum_all)
