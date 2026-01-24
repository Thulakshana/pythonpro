#multithreading use at class 
from threading import *
from time import sleep
class a(Thread): #class ekata thred kiyana class eke inherit karanna one 
    def run(self):
        for i in range(5):
            print("hello",current_thread().getName())
            sleep(1) #dilay ekak hadanawa 

class b(Thread):
    def run(self): #function name eka run kiyala denna one
        for i in range(5):
            print("welcome",current_thread().getName())
            sleep(1)


obj1=a()
obj2 = b()



obj1.start()
sleep(0.2)
obj2.start()
print('bye',current_thread().getName())