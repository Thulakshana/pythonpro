# class ekak hadana method , variable class ekata witharak seema karanawa 
#mekata private variable method use karanna puluwan

class my_class:
    x=10
    __y=20 #private variable create

    def disp(self): #private variable access karanna mehema function ekak hadanawa 
        return self.__y 

cc=my_class()
print(cc.x)
print(cc.disp())


#**********************************************************************************************************
class st2:
    def mtt(self):
        print ("public")
        self.__mt() #private method eka methanata daanawa eliyen access karanna

    def __mt(self): #private method ekak
        print("welcome")

obj=st2()
obj.mtt()



