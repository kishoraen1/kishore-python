import calc

def fun1():
    print(calc.add(5,5))
    print(__name__)
    print("From Fun1")

def fun2():
    print(__name__)
    print("From Fun2")

def main():
    fun1()
    fun2()

main()

