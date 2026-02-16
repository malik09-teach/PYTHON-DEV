print("********** Calculator **************")

def  mainproccess(a,b,sig):
    if sig == '+':
        return a+b
    elif sig=='-':
        return a-b

    elif sig =='*':
        return a*b
    elif sig =='/':
        return a//b
    else :
        return "Invalid operation"
        
        
a=int (input("enter num 1:") )
sig =input("enter sig(+,-,*,/)")      
b=int (input("enter num 2:") )

res=mainproccess(a,b,sig)
print ("Result is:",res)