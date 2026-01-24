#open file (import file)
x=open('nm.txt','r')
print(x.read())

print(x.readline())
print(x.readlines()) #text file eke thiyana ewa list ekakata ganna 
x.close() #open karapu file eka close karanwa

''''
with open('nm.txt','r') as x:
    print(x.read()) # me widihatatth puluwan (open karnnai clode karannai )
    '''


#mehema file eke wrie karoth kalin thibba ewa ain wela thamai write wenne 
y=open('nm.txt',"w")
y.write("hello\n")
y.write("bbbb")
y.close()

#thiyana data walata thawa data add karanna append use krann pulwuan

s=open('nm.txt','a')
s.write("sihara dewmini")
s.close()


kk=open('kkk.txt','w') #nathi file ekak namk dunnoth ethana ehema file ekak create wenwa 

#******************************************************************************************************
#image open karana widiha sarch karala study karanna  

