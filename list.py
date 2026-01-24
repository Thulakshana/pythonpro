#list walata values collection ekak danwa 
#create empty list
list1=[]
print(type(list1))

list2=list()
print(type(list2))


list3=[12,13,"kasun",14,15,"abc"]
print(list3[3])
print(list3.index(14))
print(list3[0:4])

list4=[12,45,67,789,["kamal","nimal"]] #list ekak athule thawa list ekak denna puluwan
print(list4[4][0]) #list ek athule thiyna list eka access karanne mehemai 

list5=["kurunagala","colombo","kandy"] #list eka athule data runtime ekedi wenas karanne mehemai 
list5[0]="galle"
print(list5)


#************************************************************************************************************
list6=[12,13,"kasun",14,15,"abc"]
list6.append("thula") #list eka awasaneta data add karanawa 
print(list6)

list6.extend(["randeepana","bhanuka"]) #extend eken apita list ekata values kihipayak add karann puluwan
print(list6)

list6.insert(0,"ravindu") #data eka list eke one thanata daanne mehemai 
print(list6)

list6.pop() #list eken data remove karanawa
print(list6)
list6.pop(0) 
print(list6)

list6.remove(12) #meken value eka dila eka remove karann puluwan
print(list6)

list6.clear() #list eka clear karanawa
print(list6)

#&*******************************************************************************************************
print(len(list4)) #list eke length eka balanawa 
print(list4.count(12)) #data ekak thiyn waara gaana hoynna meka use karanwa 

