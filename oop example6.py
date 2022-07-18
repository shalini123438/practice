from package.oopexample7 import package    #module
from abc import ABC,abstractmethod
obj=package('.py file','Any IDE')
print(obj.module)
print(obj._package__pycharm)
class educator:
    def __init__(self,len,subject):  #constructor
        self.len=len  #public
        self._subject=subject    #protected #encapsulation
class subject(ABC): #abstraction
    @abstractmethod
    def subject(self):
        return f"Python taught by sudhanshu sir"
class sir(subject):   #inheritance
    def subject(self): #method overloading
        f" sudhanshu sir teach everything in very well mannered way"
    def subject(self): #method overriding #package
        return f"i found this course amazing in vaery less cost feel so luckey thanks sir!!! "
obj1=educator(1,'python')  #object
print(obj1.len)
print(obj1._subject)
obj2=sir()
print(obj2.subject())