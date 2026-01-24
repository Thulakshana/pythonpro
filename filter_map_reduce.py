#filter function =collection ekak element walin apita one element ganna puluwan
number=[1,2,3,4,5,6,7,8]
def even_number(x):
    return x%2==0
y=list(filter(even_number,number))
print(y)

d=list(filter(lambda a:a%2==0,number)) #lamda functon eka use karala filter function eka use kaanwa 
print(d)

#**************************************************************************************************
#map function = map functon ekata mokak hari calculation ekak denwa function ekak widihata. 
#eken apita puluwan list eke thiyanwa okkoma element walata e clculation eka karanna 

number1=[1,2,3,4,5,6,7,8]
k=list(map(lambda s:s*2,number))
print(k)

#***************************************************************************************************
#reduce function = list eke thiyana okkogema sum eka ganna wage dewal
from functools import reduce
sums=reduce(lambda t,d:t+d,number)
print(sums)