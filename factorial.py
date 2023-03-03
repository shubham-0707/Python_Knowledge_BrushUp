#This is the program to calculate the factorial of a number:

n = int(input("Enter n: "))

prod = 1

for i in range(1 , n+1):
    prod = prod*i

print("Factorial is : ", prod)