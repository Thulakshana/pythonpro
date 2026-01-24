def student(subject,marks):
    print("subject =",subject)
    print("marks= ",marks)
student("maths",34)


def studentt(subject="it",marks=22,): #default argumants
    print(subject)
    print(marks)
studentt("sinahala") #default argumant waldi anith eka dila naththan uda dila thiyana eka gannawa 


def student2(subject,marks,*friends): #mehema * mark eka dunnahama e argumant ekata values kihipayak add karann apulwuan
    print(subject)
    print(marks)
    print(friends)
student2("kkk",88,"kalana","kasun")


#*******************************************************************************************************

#positional argumants
#keyword argumants
#default argumants
#variable length argumants 

#positional argumants :- variable pass karana piliwela gana salakilimath wenna one (piliwelata denna one)
def info(name,age):
    print("my name is ",name)
    print("my age is ",age)
info("kamal",23)
info(12,"kamal")

#keyword argumant 
info(age=44,name="kasun") #piliwelata denna one na. e variable nam karanna one 

#default argumants 
def info1(name,age=20):
    print(name)
    print(age)
info1("kkk") 


#variable length argumants :- hariyatama kiyala paramiter gaanak na. api pass karana values gaanata process eka wenwa 
def totall(*marks): #methanadi tuple ekak widihata thamai data store wenne 
    total=0
    for xxx in marks:
        total=total+xxx
    print(total)
totall(12,13,14)

def tt_mark(**args): #dictionary ekak widihata save wenne 
    print(args)
tt_mark(maths=23,science=44,sinhala=11)

