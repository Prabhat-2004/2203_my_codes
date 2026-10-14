from abc import ABC, abstractmethod

class Me(ABC):
    @abstractmethod
    def love_for_his(self):
        pass
    #Concrete Method
    def love_for_her(self):
        print("I Love Her More Than Everything...")

class Her(Me):
    def love_for_his(self):
        print("I Called Him Babeeeee")
i = Her()
i.love_for_her() #Invoking concrete method from the parent
i.love_for_his() #Invoking the implemented method           