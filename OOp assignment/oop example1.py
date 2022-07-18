from abc import ABC,abstractmethod
class ineuron:                                       #class
    def __init__(self,educator,course,mentor):         #constructor
        self.educator=educator
        self.course=course
        self._mentor=mentor                         #encapsulation
    def description(self):
        return f"This {self.course} is too good in less cost"
class student(ineuron):                                  #inheritance
    def student_detail(self):
        return f"Students of {self.course} is really hard working"
    def description(self):
        return f"For this {self.course} i just wanna say Big thanks to you sir"  #Method overriding
class me:
    def description(self): #method overloading
        return  f"I feel luckey to get enrolled in this course"
class datascience(ABC):
    def __init__(self,best_institute):
        self.best_institute=best_institute
    @abstractmethod                                         #abstraction
    def data(self,data):
        pass
class ineuron2(datascience):
    def data(self,data):
        print(f"In data science institute {self.best_institute} is best instute ever ")

obj=ineuron('sudhanshu sir','Full stack bootscamp','shivan')                   #object
print(obj.educator)
print(obj.course)
obj1=student('Sudhanshu sir','Data science cource','Sunny')
print(obj1._mentor)                         #encapsulation
print(obj1.description())
obj2=me()
for i in(obj1,obj2):
    print(i.description())                  #polymorphism
obj3=ineuron2('ineuron')
obj3.data('Hidden')