class Computer:
    def __init__(self):
        self.name = 'Kishore'
        self.age = 39

    def update(self):
        self.age = 30

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
c2 = Computer()

c1.name = 'Malini'
c1.age = 33
print(c1.age)
c1.update()
c2.update()
print(c1.age)
print(c2.age)

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")
#print(c1.name)
#print(c2.name)

