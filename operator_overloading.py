#Program to demonstrate the working of operator overloading...

class Student:
    def __init__(self , m1 , m2):
        self.m1 = m1
        self.m2 = m2


    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2

        s3 = Student(m1, m2)
        return s3

    def __str__(self):
        return "{} , {}".format(self.m1 , self.m2)


s1 = Student(10, 20)
s2 = Student(40, 50)

s3 = s1 + s2

#Same as printing from the below print statement...

#Here we are overloading the string type....
print(s3)

print("First: ", s3.m1 , "Second: ", s3.m2)
