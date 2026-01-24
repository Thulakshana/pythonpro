sett={1,2,3,4,5}
itr=iter(sett) #set wala data ganna widiha 
#print(next(itr))
#print(next(itr))
#print(next(itr))

while True: #while loop ekakin print karanwa itaration use karala
    try:
        print(next(itr))
    except StopIteration:
        break


