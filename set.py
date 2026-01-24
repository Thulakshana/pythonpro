#set= unorder data type 
#set ekaka unique vlaues witharai thiygnn puluwan 
#index number use karala values hoyaganna ba 

set0={'thilini','nadeesha',2017,2015}
print(type(set0))
print(set0)

list1=[1,2,3,4]
set1=set(list1) #me widihata list ekak set  ekak widihata convert karanna puluwan

set0.add("wickramasinghe")#set ekakata aluthin data add karahaki 
print(set0)


#*************************************************************************************************************
a={1,2,3,4,5,6,7,70}
b={2,4,3,5,6,7,8,90}

print(a.union(b)) #a walai b walai thiyana okkoma values 
print(a.intersection(b)) # a walatai b walatai podu tika
print(a.difference(b)) #a wala witharak thiyana tika
print(b.difference(a))#b wala witharak thiyan tika 

#***********************************************************************************************************

set0.add("suba")
print(set0)

set0.update(["football","cricket"]) #set ekata multiple values add karanawa
print(set0)

set0.remove("football") 
print(set0)

