#create random numbers 
import random
x=random.random()*10
print(x)


y=random.uniform(1,10)
print(y)


anim=['kaml','saman','amal'] #list ekakin random name gannawa 
winner=random.choice(anim)
print(winner)

numm=list(range(1,10))
print(numm) 
random.shuffle(numm) #random anannad 
print(numm)