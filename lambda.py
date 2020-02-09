from functools import reduce

#f = lambda a, b,c,d: a + b * a * b * (c / d) + d

#result = f(5, 6, 8.5, 3.4)

#print(result)

nums_list = [3,2,6,4,2,5,7]

evens_list = list(filter(lambda n : n%2==0,nums_list))
odd_list = list(filter(lambda n : n%2!=0,nums_list))

evens_tuple = tuple(filter(lambda n : n%2==0,nums_list))
odd_tuple = tuple(filter(lambda n : n%2!=0,nums_list))

evens_set = set(filter(lambda n : n%2==0,nums_list))
odd_set = set(filter(lambda n : n%2!=0,nums_list))

doubles_list = list(map(lambda n : n*2, evens_list))

print(doubles_list)
print (evens_list)
#print(evens_tuple)
#print (evens_set)
