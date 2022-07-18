from abc import ABC,abstractmethod
import oop3       #module
print(oop3)
class me:    #class
    def __init__(self,name,age,height):   #constructor
        self.name=name
        self.age=age
        self.__height=height #encapsulation
    def s(self):
        return f"im student of ineuron"
class timing(ABC): #inheritance
    @abstractmethod  #abstraction
    def timing(self):
        f"Timing of class is 3 to 6"
class time(timing):   #inheritance
    def timing(self): #polymorphism     #method overrding
        f"Timing of class is 3 to 6 and 6 to 9 is daubt clearing session"
    def timing(self): #method overriding
        return f"nothing"
obj=me('shalu',22,5.4)
print(obj.age)
print(obj.name)
print(obj._me__height)
