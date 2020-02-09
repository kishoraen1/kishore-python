num = int(input("Enter number of your choice = "))

for i in range(2,num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print ("Prime")