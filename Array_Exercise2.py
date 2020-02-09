from array import *

arr = array('i',[])

n = int(input("Enter the Array length of your wish = "))

for i in range(n):
    x = int(input("Enter the Value = "))
    arr.append(x)

 # print (arr[0])
print(arr)

for j in range(len(arr),0,-1):
    print (arr[j-1])


