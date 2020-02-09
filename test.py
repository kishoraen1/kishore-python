from functools import reduce

def add_all(a,b):
    return a + b


nums = [1,2,3]
sums = reduce(add_all,nums)

print(sums)
