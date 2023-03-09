#Program to demonstrate the working of method overriding...


class A:
    def show(self):
        print("We are in show function of class A")


class B(A):
    def show(self):
        print("We are in show functio of class B")


b = B()
print(b.show())