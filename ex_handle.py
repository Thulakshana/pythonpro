#exeption handdle= run time eke usergen wenna puluwan waradi hadanna
try:
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    print(a/b)
except ZeroDivisionError as e: #api enna puluwan error ekak identify karala denwa
    print("cannot devide by zero")
except Exception as e: #meka witharak athi danata 
    print("went wrong",e)
finally:
    print('bye')


