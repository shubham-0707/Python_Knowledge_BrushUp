#Program to find the last valid fibonacci number...

# This is the code....
def validFibo(n):
    a = 0
    b = 1

    c = 0
    while c<n :
        c = a+b
        a=b
        b = c

    return a

print(validFibo(55))

