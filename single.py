class Demo1:
    def disp1(self):
        print("Its Demo1")

class Demo2(Demo1):
    def disp2(self):
        print("Its Demo2")

d1 = Demo1()
d1.disp1()
d2 = Demo2()
d2.disp1()
d2.disp2()