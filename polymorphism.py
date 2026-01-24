#polymorphism = ekama deyak wiwida akarayen thiynwa (many forms)
#method overloading 
#method overriding 
#opeartors overloading 

#method overriding = method dekak thiynwa, nama sanamai, karanne task 2k 

class parent:
    x=12
    def func(self):
        print("helo")
class child(parent):
    def func(self):
        print("welcome")

myobj=child()

print(myobj.func())


#method overloading 
class cal:
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            sum=a+b+c
            print(sum)
        elif a!=None and b!=None:
            sum=a+b
            print(sum)
        else:
            sum=a
            print(sum)



obj=cal()
obj.add(2,3)