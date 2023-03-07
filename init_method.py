#This program is made to demonstrate the working of init method...

class Student:
    def __init__(self , name , rollNo):
        self.name = name
        self.rollNo = rollNo

    def info(self):
        print("Student is: ", self.name, self.rollNo)




s1 = Student("Shubham", 1904220100103)
s2 = Student("Mukul", 1904220100074)

s1.info()
s2.info()




