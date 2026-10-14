from abc import ABC , abstractmethod
'''Rule-1: We can create an object for empty abstract class...'''
class Animal1(ABC):
    pass
a1 = Animal1()


'''Rule-2:If abstract class contain abstract method then object for that abstractmethod then object for that 
abstract class cannot be created and abstract method cannot be invocked(called it)'''
class Animal2(ABC):
    @abstractmethod
    def eat(self):
        pass
#a2 = Animal2() #Can't instantiate abstract class Animal22 without an implementation for abstract method 'eat'

'''Rule-3: If abstract class contains only concrete method, then obejct can be created and method can be invoked(called)'''
class Animal3(ABC):
    def eat(self):  #----Concrete Method
        print("Inside eat")
a3 = Animal3() #-------Creating an object
a3.eat() #------------Invoking concrete method


'''Rule-4: If class id derived from abstract class and not given body for all abstract methods in 
child class object cannot be created'''
class Animal4(ABC):
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def sleep(self):
        pass
class Child(Animal4):
    def eat(self):
        print("Inside eat..")
#Creating object for Man class
#a4 = Child() #Can't instantiate abstract class Child without an implementation for abstract method 'sleep'



'''Rule-5: If a class  have both abstract and concrete method, then object cannot be created for that class...'''
class Animal5(ABC):
    @abstractmethod
    def eat(self):
        pass
    #Concrete Method
    def sleep(self):
        print("In Sleep...")
a5 = Animal5()
