from array import *

arr = array('i',[])

n = int(input("Enter the Array length of your wish = "))

for i in range(n):
    x = int(input("Enter the Value = "))
    arr.append(x)

print (arr)

val = int(input("Enter the search key = "))

print(arr.index(val))



