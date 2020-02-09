def name_count(lst1):
    count = 0
    for e in lst1:
        if len(e) > 6:
            count += 1
    return count


lst = ['Kishore', 'Malini', 'Lakshana', 'Taishka','Kumar','Geetha']
names = name_count(lst)
print("List of Names where is greater than 6 = ", names)
