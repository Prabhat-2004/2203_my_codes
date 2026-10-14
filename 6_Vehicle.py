class Vehicle:
    def __init__(self, Vehicle_type):
        self.vehicle_type = Vehicle_type
    def info(self):
        print(f"Vehicle Type: {self.vehicle_type}")
class Car(Vehicle):
    def __init__(self,Vehicle_type,brand):
        self.brand = brand
        super().__init__(Vehicle_type)
    def details(self):
        print("Vehicle Type:", self.vehicle_type)
        print("Brand:",self.brand)
c = Car("4_Wheeler","Tayota")
c.details()