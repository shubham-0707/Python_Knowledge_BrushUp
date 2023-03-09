#This is the program to demonstrate the working of the iterator...

class TopTen:

    def __init__(self):
        self.m1 = 1

    def __iter__(self):
        return self

    def __next__(self):
        if(self.m1<=10):
            val = self.m1
            self.m1+=1
            return val
        else:
            raise StopIteration


values = TopTen()

for i in values:
    print(i)
