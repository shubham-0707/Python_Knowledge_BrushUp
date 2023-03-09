#This program is made to demonstrate the working of Duck Typing...

class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class IntelliJ:
    def execute(self):
        print("Spell Check")
        print("Code Format")
        print("Compiling")
        print("Running")
class Duck:
    def work(self , ide):
        ide.execute()


d1 = Duck()
d1.work(PyCharm())
d1.work(IntelliJ())

