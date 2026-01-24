name="thulakshana"
print(name)
print(name[4])
print(name[1:4])
print(name[-1])

s1='python'
s2='programming'
s3=44
print(s1+s2) 
print(s1+s2+str(s3)) #string me widihata ekathu karanakota wena data type string walata convert karanna one 

address="buluwala"
print("b" in address) #mokak hari character ekak thiyanwada kiyala balanna meka use karanawa 
print("z" not in  address)

#****************************************************************************************************************
#string methods 
cla='thula dissa'
print(cla.upper())
print(cla.lower())
print(cla.title()) #hama word ekema palaweni akura capital
print(cla.capitalize())

#**************************************************************************************************************
#find()
print(cla.find('d'))
print(cla.find('d',3,7)) # 3=patan ganna thana 7=end wena thana

print(cla.index('d')) #index eka ganna

print(cla.center(20,"-")) #allignment fix karanawa 
print(cla.rjust(60,"-")) #dakunu paththata allign wenwa 

#***********************************************************************************************************

st="thulakshana dissanayaka"
print(st.startswith("t"))
print(st.startswith("thulakshana")) #patan ganna thana
print(st.endswith("dissanayaka")) #iwara wena thana

xx="kamal,22,colombo"
print(xx.replace(",","-")) #mokak hari replace karanna meka use karawa 

vv='abc'
nn='xyz'
print(vv.join(nn)) #string dekak ekata ekathu karanawa 

na=["kamal","nimal","udara"]
print("-".join(na))





