''' 
this programs is fir the testing
'''
print ("hello world ")


print("for nested")

for i in range(3):

     for k in range(5):
       
        print(f"{i}*{k}=",i*k)
                 
     
                           
    
print("while nested")





i = 0
while i < 3:
    k = 0
    while k < 4:
        print(f"{i}*{k}=", i * k)
        k += 1
    i += 1