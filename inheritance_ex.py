#super()
#method overriding 

class parent:
    def func1(self):
        print("hello")

class child(parent):
    def func2(self):
        super().func1() #eka function ekakin function dekak call karanna super function eka use karanawa
        print("hello2")

obj=child()
obj.func2()

#method overriding 
class pr:
   def fun1(self):
      print("fun1")
class ch(pr):
    def fun2(self):
        print("fun2")
    def fun1(self):
        print("fun3")

bb=ch()
bb.fun1()




