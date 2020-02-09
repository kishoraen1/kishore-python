def person(name, age=18):
    print("Name: ", name)
    print("Age: ", age)


# person(name = 'Kishore', age=39)

def sum(*b):
    c = 0
    for i in b:
        c = c + i

    print(c)

sum(5, 6, 34, 78)
