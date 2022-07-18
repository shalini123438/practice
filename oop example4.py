from abc import ABC,abstractmethod
class ineuron(ABC):     #class
    def __init__(self,educator,mentor,mentor_earning): #constructor
        self.educator=educator
        self.mentor=mentor
        self._mentor_earning=mentor_earning          #encapsulation

    def quality(self): #method
        return f"ineuron provide qualiyu eduction"
class syllabus(ineuron): #inheritance
    def __init__(self,no_of_subject,year_of_completion):
        self.no_of_subject=no_of_subject
        self.year_of_completion=year_of_completion
    def quality(self):          #method overloading
        return f"i'm also a student of{self.educator}"
class abstraction(ABC):
    @abstractmethod              #abstraction
    def abstraction(self):    #polymorphism
        return f"It hide the complexity"
class sub_abstraction(abstraction):
    def abstraction(self):     #method overriding
        return f"Give the functinallity to use that"
obj=ineuron('Sudhanshu','sunny',80000) #object
print(obj.educator)
print(obj.mentor)
print(obj._mentor_earning)
obj2=sub_abstraction()
print(obj2.abstraction())
obj3=syllabus(8,1)
print(obj3.year_of_completion)