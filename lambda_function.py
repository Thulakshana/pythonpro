#meka namk nathi function ekak 


def area(x): #normal function eka
    return x*x
print(area(4))

area2=lambda y:y*y #lambda function eka 
print(area2(5))

#lambda function ekak normal function wala use karana widiha 
def apple(unit_price):
    return(lambda number_of_apple:unit_price*number_of_apple)
g=apple(10) 
print(g(20))
