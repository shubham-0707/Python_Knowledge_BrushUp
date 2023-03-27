
# In this problem I have to find out the length of the largest substring which do not contain any duplicate
# characters...


string = input("Enter string: ")
maxi = -99

for i in range(0, len(string)):
    for j in range(i+1, len(string)):
        temp = string[i:j]
        if len(set(temp))==len(temp):
            maxi = max(maxi, len(temp))


print("The largest substring length is : ", maxi)