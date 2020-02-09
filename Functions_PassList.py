def count_odd_even(lst1):
    odd = 0
    even = 0

    for i in lst1:
        if (i % 2) == 0:
            even += 1
        else:
            odd += 1
    return odd,even


lst = [21, 43, 65, 32, 342, 545, 3453, 445]
odd,even = count_odd_even((lst))
print("Total Odd Numbers = ", odd)
print("Total Even Numbers = ", even)
