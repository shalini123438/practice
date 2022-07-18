from abc import ABC,abstractmethod
class student(ABC):         #inheritance
    def __int__(self,name,course):  #constructor
        self._name=name   #encapsulation
        self.course=course

    @abstractmethod  # abstraction
    def student_details(self):
        f'student should be hardworking'
class ineuron(student):
    def student_details(self): #method overriding
        return f'I neuron always provide quality education' #polymorphism
    def student_details(self): #method overloading
        return f"Quality education for all student without any biasness"
obj2=ineuron()         #object
print(obj2.student_details())
