class Demo1:
    def disp(self):
        print("In Demo1")
class Demo2:
    def disp(self):
        print("In Demo2")
class Demo3(Demo1,Demo2):
    pass
d3 = Demo3()
d3.disp()
print(Demo3.__mro__) #(<class '__main__.Demo3'>, <class '__main__.Demo1'>, <class '__main__.Demo2'>, <class 'object'>)