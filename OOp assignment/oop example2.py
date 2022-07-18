from abc import ABC,abstractmethod
class ineuron: #class
    def __init__(self,course_name,year,price):  #constructor
        self.course_name=course_name
        self.year=year
        self._price=price #encapsulation
    def need(self):                           #method
        return f"for this {self.course_name} The only thing which is need is effort only"
class new_batch(ineuron): #inheritance
    def __init__(self,start_date,end_date):
        self.start_date=start_date
        self.end_date=end_date
    def need(self):         #Method overloading
        return f"In this course {self.course_name} ineuron giving their 100% effort"
    def need(self):                                      #method overriding
        return f"End of the day you are only who can push you for yourself"
class student(ABC):
    @abstractmethod                         #abstraction
    def student(self):
        f"ineuron student are smart because if he can enroll in i neuron we can understand how much all are smart"
class student_length(student):
    def __init__(self,student_lenth):
        self.student_lenth=student_lenth
    def student(self):        #polymorphism
        f"Student are smart but just because of teacher and mentor of ineuron"
obj=ineuron('Full stack data science',2022,1800)   #object
print(obj.need())
print(obj.course_name)
print(obj.year)
print(obj._price)
obj2=new_batch(2022,2023)
#print(obj2.course_name)
print(obj2.start_date)
print(obj2.end_date)
print(obj2.need())
for i in(ineuron,new_batch):
    print(i.need)
obj3=student_length(3000)
print(obj3.student())