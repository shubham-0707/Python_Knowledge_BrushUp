#Program to find the last valid fibonacci number...


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

