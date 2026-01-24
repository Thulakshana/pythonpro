#abstract method= content ekak nathi method ekak 
#abstract clss= abstract method thiyana class ekak
#abstract class walata object create karanna ba 


from abc import ABC,abstractmethod #ABC= abstract based class
class phone (ABC): #abc modul eka inherit karanawa 
    @abstractmethod #create abstract method
    def func(self):
        pass

class samsung(phone):
    def func(self):
        pass



