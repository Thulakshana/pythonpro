#serialize= function wag edewal kata hari yawanna wenama store karala thiyagannawa 
#de serializing = e function nawatha use karana eka 

#json = json kyanne hama programming language ekak ekkama wada karanna puluwan serialization module ekak 
#json waladi class , function wage dewal serialize karanna ba. pickle walin puluwan 
#json waladi data store wenne text ekak widihata. pickele ekka binary format eken store wenwa 
#pickle = pickele use karanna puluwn python walata witharai 

import pickle
data={"name":"thula","age":"23"}
filename="dict.pickle"
with open(filename,"wb") as f:#create karana file eke nama, open karana mode eka
    pickle.dump(data,f)

