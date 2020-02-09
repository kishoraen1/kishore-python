class A:
    def feature1(self):
        print ("Feature1 Working")
        print(__name__)

    def feature2(self):
        print ("Feature2 Working")

class B(A):
    def feature3(self):
        print("Feature3 Working")
        print(__name__)

    def feature4(self):
        print("Feature4 Working")

a1 = A()
b1 = B()
b1.feature3()
b1.feature1()