# this program is made to print from 1 to 100 and skipping the multiples of 3 and 5

for i in range(1 , 101):
    if(i%3==0 or i%5==0):
        continue
    print(i, end=" ")