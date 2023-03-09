#This program is made to demonstrate the file handling process in Python...

f1 = open("abc.txt", "w")
f1.write("Hello Shubham Singh")
f1.write("How are you ?")
f1.write("I am good")
f1.write("I am also good")

f1 = open("abc.txt", "r")
f2 = open("pqr.txt", "w")

for data in f1.readlines():
    f2.write(data)

f2 = open("pqr.txt" , "r")
for i in f2.readlines():
    print(i)


