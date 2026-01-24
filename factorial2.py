#factorial using recursion 
#recursion = function ekak athuledi e function ekatama nawatha nawatha call karanwa 

#4!=4*3*2*1
#4!=4*3!
#4!=4*(4-1)!
#n!=n*(n-1)!

# 0 factorial eka 1i
# factorial eka claculate karanna puluwan dana (positive) anka walata witharai 

def factt(n): #factorial eka hoyanna one value eka
    if n==0: #n==0 unahala factorial eka ekai (0 factorial eka 1 wena hinda)
        return 1
    else:
        return n*factt(n-1)
print(factt(24))