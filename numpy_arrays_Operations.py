from numpy import *
from array import *
# array

arr1 = array('i',[1,10,3,24,5])
arr2 = array('i',[1,2,3,4,5])
arr3 = array('i',[])

for e in range(0, len(arr1)):
    arr3.append (arr1[e] + arr2[e])

print(arr3)

max = 0
for i in range(0,len(arr1)):
    if max > arr1[i]:
        continue
    else:
        max = arr1[i]
print (max)









