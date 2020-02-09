x = int(input('How may Candies you want ? = '))
av = 5
i = 1

while i<= x:

    if i > av:
        print("Out of Stock")
        break
    print("Candy")
    i+=1


for j in range(6):
    if j == 0:
        break
    print("Hello ", j)
