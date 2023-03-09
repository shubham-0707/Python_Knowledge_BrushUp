#This program is used to demonstrate different types of variables in OOPs...

class Student:

    school = "Green Field Academy"

    def __init__(self , m1 , m2 , m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def schoolName(cls):
        return cls.school

    @staticmethod
    def aiseHi():
        print("Hello this is just a fake function")


s1 = Student(10, 20, 30)
s2 = Student(30, 40 , 50)

print(s1.avg())
print(s2.avg())

print(Student.schoolName())
Student.aiseHi()
