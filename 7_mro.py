class demo1:
    def disp1(self):
        print("Inside demo1")
class demo2:
    def disp2(self):
        print("Inside demo2")
class demo3(demo1,demo2):
    def disp3(self):
        print("Inside demo3")

d3 = demo3()
d3.disp3() #Inside demo3
d3.disp2() #Inside demo2
d3.disp1() #Inside demo1
print(demo3.__mro__) #(<class '__main__.demo3'>, <class '__main__.demo1'>, <class '__main__.demo2'>, <class 'object'>)
print(demo2.__mro__) #(<class '__main__.demo2'>, <class 'object'>)
print(demo1.__mro__) #(<class '__main__.demo1'>, <class 'object'>)