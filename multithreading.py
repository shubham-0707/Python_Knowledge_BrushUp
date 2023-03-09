# this program is made to demonstrate the working of threads....

from threading import *
from time import sleep


class Thread1(Thread):
    def run(self):
        for i in range(10):
            print(" Hello")
            sleep(1)


class Thread2(Thread):
    def run(self):
        for i in range(10):
            print(" Hi")
            sleep(1)



t1 = Thread1()
sleep(0.2)
t2 = Thread2()

t1.start()
t2.start()

t1.join()
t2.join()


print("Bye")




