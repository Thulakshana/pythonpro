#procedure programming language :- basic widht use karanne function 
#object oriented programming :- class use karanawa 
#object= attribute + methods (function)

class phone: #create class
    #attribute denne variable ekak widihata 
    #methods denne function ekak widihata 
    pass #empty class ekak 


class ph1:
    def say(self,name):
        print("hello",name)

phone1=ph1() #create object 

phone1.say("nokia")

class ph2:
    def say2(self,name):
        self.x=name #class ekak athule hadana attribute pitin dena object walata connect karanna self use karanawa 

phone2=ph2()
phone2.say2("ssss")
print(phone2.x)
phone2.x="kd" #variable pitin access karanawa 
print(phone2.x)

