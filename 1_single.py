class Father:
    def talk1(self):
        print("Father can talk...")
class Son(Father):
    def talk2(self):
        print("Son can talk....")
s = Son()
s.talk1()
s.talk2()