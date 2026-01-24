#tuple waladi runtime ekedi values wens karanna ba 
tp1=('kamal',12,"kandy",'false',11)
print(type(tp1))
tp2=tuple() #create empty tuple

print(tp1[1])
print(tp1.count(11)) #data use una waara gaana
print(tp1.index(12)) #index eka 

list1=[12,11,22,33,44,55] #list eka tupple ekak walata convert karanawa 
tpl=tuple(list1)
print(tpl)
