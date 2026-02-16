import numpy as np   

arr1d=np.array([])

while number != '\n':
    number =int (input("enter number "))
    arr1d=np.append(arr1d,number)


for i in range(len(arr1d)):
    print("Element at index",i,"is",arr1d[i])

