#This program is made to check the perfect square number...

import math

for i in range(1 , 51):
    a = int(math.sqrt(i))
    if(a*a==i):
        print(i, end=" ")