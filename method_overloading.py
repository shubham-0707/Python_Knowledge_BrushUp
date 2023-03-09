#this program is made to demonstrate the working of Method Overloading...

class A:
    def add(self , a=None, b=None, c=None):
        if(a!=None and b!=None and c!=None):
            return a+b+c
        elif(a!=None and b!=None):
            return a+b
        else:
            return a


#This is how method overloading is done in Python....

a = A()
print(a.add(6))