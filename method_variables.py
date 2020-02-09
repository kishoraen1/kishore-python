class Student:

    school = 'VDS Jain'

    def __init__(self,EnglishMark,ScienceMark,MathsMark):
        self.EM = EnglishMark
        self.SM = ScienceMark
        self.MM = MathsMark

    def avg(self):
        return (self.EM + self.SM + self.MM)/3

    @classmethod
    def info(cls):
        return (Student.school)

#EnglishMark = int(input("Enter English Mark = "))
#ScienceMark = int(input("Enter English Mark = "))
#MathsMark = int(input("Enter English Mark = "))

s1 = Student(80,90,100)
s2 = Student(75,65,45)

print(s1.avg())
print(Student.info())
print(s2.avg())