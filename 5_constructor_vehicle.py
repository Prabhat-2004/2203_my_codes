class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def car(self):
        if self.status == "Rented":
            print(f"{self.make} {self.model} marked has been rented.....")
    
        print(f"Make: {self.make}, Model: {self.model}, Status: {self.status}")

v1 = Vehicle("Honda","Civic")
v2 = Vehicle("Honda","Civic")
v1.status = "Available"
v2.status = "Rented"
v1.car()
v2.car()