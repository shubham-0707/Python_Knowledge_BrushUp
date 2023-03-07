# This program is made to demonstrate the use of self variable...

class Student:

    def __init__(self):
        self.name = "Shubham"
        self.age = 20

    def update(self):
        self.age = 25

    def info(self):
        print("Age: "+self.age+"\n"+"Name: "+self.name)

    def compare(self, other):
        if self.age==other.age:
            print("They are same")
        else:
            print("They are different")



s1 = Student()
s2 = Student()

s1.update()

s1.compare(s2)


