#This is the program to demonstrate the working of abstract classes...

from abc import ABC , abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("It is running")


class Programmer:
    def work(self , com):
        print("I am working")
        com.process()

com1 = Laptop()

Programmer.work(com1)