#multitreding = ekapaara wada godak kireema (ex:- functon dekak eka paara run weema)

import threading #meka import karaganna one
from time import sleep
def func1():
    for i in range (5):
        print("good")
        sleep(1)

def func2():
    for i in range (5):
        print("byee")
        sleep(1)
t1=threading.Thread(target=func1) #function walata thred create karanawa 
t2=threading.Thread(target=func2)

t1.start()
sleep(0.2)
t2.start()

