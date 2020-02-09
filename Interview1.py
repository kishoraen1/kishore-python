def unique_names(names1, names2):
    set1 = {}
    set2 = {}
    names3 = []
    set1 = set(names1.copy())
    set2 = set(names2.copy())
    set3 = set1.union(set2)
    names3 = list(set3.copy())
    names3.sort()
    return names3

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1,names2))
#print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia