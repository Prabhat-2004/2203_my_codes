class Demo1:
    def magic(self):
        print('Magic inside Demo1')
class Demo2:
    def magic(self):
        print('Magic inside Demo2')
class Demo3(Demo2,Demo1):
    pass

d3 = Demo3()
d3.magic()
print(Demo3.mro())