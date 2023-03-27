# In this problem I have to print a pattern based on the given input...

n = int(input("Enter n : "))

x = n
for i in range(n):
    for j in range(x):
        print("*", end=" ")
    x= x-1
    print()


