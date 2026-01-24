import pickle
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
person_obj=person("kasun",22)

#create pickel file 
with open("class_pickele_file","wb")as f:
    pickle.dump(person_obj,f)
         
        