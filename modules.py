import calc
print(__name__)
req = input("Enter your choice of Operation = ")

if req == "add":
    num1 = int(input("Enter your first number = "))
    num2 = int(input("Enter your second number = "))
    print(calc.add(num1,num2))
elif req == "sub":
    num1 = int(input("Enter your first number = "))
    num2 = int(input("Enter your second number = "))
    print(calc.sub(num1,num2))
elif req == "mul":
    num1 = int(input("Enter your first number = "))
    num2 = int(input("Enter your second number = "))
    print(calc.mul(num1,num2))
elif req == "div":
    num1 = int(input("Enter your first number = "))
    num2 = int(input("Enter your second number = "))
    print(calc.div(num1,num2))
else:
    print("Not a valid Operation")
