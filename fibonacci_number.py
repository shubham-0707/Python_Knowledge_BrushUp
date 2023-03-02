#this is the program to print the first n fibonacci numbers...

def fibo(n):
    a = 0
    b = 1
    if(n<1):
        print("Invalid Input")
        return
    elif(n==1):
        print(a)
    else:
        print(a)
        print(b)
        for i in range(n-2):
            c = a+b
            print(c)
            a = b
            b = c


n = int(input("Enter n : "))
fibo(n)


