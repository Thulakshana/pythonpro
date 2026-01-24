
#meka hariyatama na meka check karala balanna

def new(func):
    def inside(a,b):
        if b==0:
            a,b=b,a
            return func(a,b)
        return inside


def devide(a,b):
   # if b==0: # b walat assign karana value eka 0da balanwa 
    #    a,b=b,a #a=b b=a
    return a/b


devide=new(devide)
print(devide(5,0))


