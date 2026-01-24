def test():
    #return 4 #return wenuwat yield use karanwa 
    yield 4 #genarator ekak karanna 

y=test()
print(next(y)) #return value display karanna(yeild)


print(test())


#list walata use karanwa 
def lll(a):
    for i in a:
        yield i
h=lll([2,4,6,8])
print(next(h))


#create fibonaci using genaraters 
def fib():
    a=0
    b=1
    while True:
        c=a+b
        yield a
        a,b=b,c


yy=fib()
print(next(yy))
print(next(yy))






