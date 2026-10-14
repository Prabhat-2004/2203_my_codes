class Demo1:
    def __init__(self):
        self.x = 100
class Demo2:
    def __init__(self):
        self.x = 200
        Demo1.__init__(self)
class Demo3(Demo2,Demo1):
    pass
d = Demo3()
print(d.x) #100