## the variable in pythin is case sensittive 
## the varible take atou data type as the value assigned to it
## the valve and data type can be changed at any time
## addresses of the variable can be checked using id() function



## let example 


a = 10
b = 20  


#case senseitiv

A= 40
B =50



## printing all  varaibles 
print ("a=",a, "\n b=",b, "\n A=",A ,"\n B=",B,"\n")


## checkiing the variables case sensitivity 

isequal1=A==a
print ("A is equal to a :",isequal1)
isequal2=B==b
print ("B is equal to b :",isequal2)


## same value different variable checking
c= 40 
c==A
print ("c is equal to A :", c==A)


## address of the varaible 

print ("Value of a is: ", a, " and id of a is: ", id(a))
print ("Value of b is: ", b, " and id of b is: ", id(b))
print ("value of A : ",A , "id of A is :",id(A))
print ("value of c : ",c , "id of c is:",id(c))


## assigning the diff value to the a same variable and the data type will change only 


# let 

A = " malik abbas khan "

#checking the  name and the address
print ("value of A : ",A , "id of A is :",id(A))


