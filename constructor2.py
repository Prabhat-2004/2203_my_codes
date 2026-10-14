class student:
    def __init__(self,name,id):
        self.st_name = name
        self.st_id = id
    def learn(self):
        print(f"{self.st_name}  is learning and her/his ID is {self.st_id}")
    def play(self):
        print(f"{self.st_name}  is playing and her/his ID is {self.st_id}")
    def st_details(self):
        print(f"Student Details:-")
        print(f"Student Name: {self.st_name}")
        print(f"Student ID: {self.st_id}")
        print()

s1 = student("Ak",101)
s2 = student("Pk",102)
s3 = student("Rk",103)
s4 = student("Pp",143)
s1.learn()
s1.st_details()
s2.play()
s2.st_details()
s3.learn()
s3.st_details()
s4.play()
s4.st_details()