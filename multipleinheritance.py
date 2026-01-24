class ca1:
    def feature1(self):
        print("class 1")

class ca3:
    def feature3(self):
        print("class 3")

class ca2(ca1, ca3):  # multiple inheritance 
    def feature2(self):
        print("class 2")

obj = ca2()
obj.feature1()
