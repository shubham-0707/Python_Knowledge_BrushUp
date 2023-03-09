#this program is used to demonstrate the working of inner class...

class Student:

    def __init__(self, name, rollNo):
        self.name = name
        self.rollNo = rollNo
        self.laptop = self.Laptop()


    def show(self):
        print("name: ", self.name)
        print("rollNo: ", self.rollNo)
        #print("laptop: ", self.laptop)

    class Laptop:
        def __init__(self):
            self.name = "Asus"
            self.ram = "8 GB"
            self.processor = "i5"

        def show(self):
            print("Name: ", self.name)
            print("RAM: ", self.ram)
            print("processor: ", self.processor)


s1 = Student("Shubham", 123)
print(s1.show())

obj = s1.Laptop()

print(obj.show())