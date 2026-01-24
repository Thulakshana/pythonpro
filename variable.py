#variable = mokak hari data ekak store karala thiyaganna dena namak
name="thulakshana"
age=12
weight=12.4
print(name)
print(age)
print(type(name))

address,school,height="colombo","buluwala",12.8
print(address,school,height)

mango=apple=orange=50 
print(mango,apple,orange)

i_am="thula"
i_am="dissa"
print(i_am)

#case sensitive 
mm="tt"
MM="kk"
print(mm)
print(MM)

#data type 
kk=[1,"td",12.5] #list wala data type kihipayak thiyaganna puluwan
print(kk)
td=(2,3,4,5) #tupple ekaka values aya wenas karanna ba
print(td)
set={1,2,3} #set kiyanne kulakayak #meke thiyaganna puluwan unique values withrai (ekama value eka aye thiyanna ba)

cs=123
print(type(cs))
print(cs.__sizeof__())


tr=True
ff=False
print(tr,ff)

#complex number
com=4j #4=real j=imagenary 
print(type(com)) 
print(com.real) #real part eka
print(com.imag) #imaganary part eka

#dynamically type language 
#variable wala type wenas wena hinda thamai dynamically kiynne (kalin define karala thiyana variable ekakata unath run time ekdi wena type ekka values assign karanna puluwan )
#java wage language wala meka bari hinda statically type wenawa 
x=25
print(type(x))
x=45.67
print(type(x))
x="dissnayaka"
print(type(x))

#arithmatic operators 
print(5//2) #floor division 
print(5%2) #modulas
print(2**2) #power 

print((5%4)*2+(6//4)) 

a=4
b=3
print(a>b)
print(a<b)
print(a!=b)

one=22
two=33
print((one>10)and(two>10))
print((one>25)or(two>25))

print(True and True)
print(False and True)
print(True or False)
print(True or True)
print(not True)


math_marks=45
science_mark=43
attendance=88
print((math_marks>44 or science_mark>44)and attendance>500)

#identity operators 
#data store wela thityenne ekama memory location ekeda kiyala balanawa 
x=10
y=10
z=8
print (x is y) #is walin memory address samanaida kiyala check karanawa
print(x is not y)
print(id(x)) #variable eka save vela thiyana location eke id eka gannawa
print(id(y))
print(id(z))

g=[1,2,3] 
h=[1,2,3]
print(g is h)
