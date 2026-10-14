class User:
    bank = "SBI" #Class Label Veriable / Static Veriable
    def deposite(self):
        print(f"{self.name} Is Deposite Money({self.money}) In Account No.-{self.acc}({p1.bank})")
    def withdraw(self):
        print(f"{self.name} is Withdraw Money({self.money}) from Account No.-{self.acc}({p2.bank})")

p1 = User()
p2 = User()
p1.name = "Preeti" #>>>>>>>>>>>>>>>>>>>>>(Instance Veriable)
p1.acc = 143 #>>>>>>>>>>>>>>>>>>>>> (Instance Veriable)
p1.money = 25000 #>>>>>>>>>>>>>>>>>>>>>(Instance Veriable)
p2.name = "Prabhat" #>>>>>>>>>>>>>>>>>>>>>(Instance Veriable)
p2.acc = 1432 #>>>>>>>>>>>>>>>>>>>>>(Instance Veriable)
p2.money = 25000 #>>>>>>>>>>>>>>>>>>>>>(Instance Veriable)
p1.deposite() 
p2.withdraw()

