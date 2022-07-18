from abc import ABC,abstractmethod
import oop3 #module
print(oop3)
class package:   #class
    def __init__(self,module,pycharm):  #constructor
        self.module=module  #public
        self.__pycharm=pycharm   #private #encapsulation
    def package(self):
        return f"one or more module or colection of module inside folder or directory is called as a package"
class internship(package):  #inheritance
    def __init__(self,year):
        self.year=year
    def package(self):   #method overloading
        return f"Example of package is:company offer us package which is collection o in hand salary,house allowence, basic salary etc"
    def package(self):  #polymorphism, #method overriding
        return f"package is collection of something"
class student(ABC):  #abstraction
    @abstractmethod
    def student(self):
        f"Student got package from company"
class top(student):
    def student(self):
        return f"Top student got highest package because they work hard"
obj=package('Any .py file','IDE')
print(obj.module)
print(obj._package__pycharm)
print(obj.package())
obj1=internship('1 year')
print(obj1.package())