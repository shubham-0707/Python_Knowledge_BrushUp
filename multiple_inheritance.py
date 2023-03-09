#this program is made to demonstrate the working of multiple inheritance...

class A:

    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")


class B:

    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

class C(A , B):

    def feature5(self):
        print("Feature 5 is working")

    def feature6(self):
        print("Feature 6 is working")


c = C()
c.feature4()
c.feature6()
c.feature1()