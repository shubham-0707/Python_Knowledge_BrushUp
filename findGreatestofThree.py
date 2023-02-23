# this is the program to find out the greatest number among the 3 numbers...

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if(a>b and a>c):
    print("{} is the greatest number ".format(a))
elif(b>c and b>a):
    print("{} is the greatest number ".format(b))
else:
    print("{} is the greatest number ".format(c))