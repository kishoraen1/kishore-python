a = 10
print(a)
print(id(a))

def something():
    x = globals() ['a']
    print (id(x))

    a = 9
    print("In Func", a)

    globals()['a'] = 15


something()

print("Outside", a)
