def person(name, **data):
    print("Name : ", name)

    for i,j in data.items():
        print (i.capitalize(), ": ",j)

person('Kishore', age=39, city = 'Pune', Mob = 7768022822)
