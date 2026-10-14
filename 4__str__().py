class Point:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return f"({self.a}, {self.b})"
    def __add__(self,other):
        return  Point(self.a +other.a, self.b + other.b)

p1 = Point(2,3)
p2 = Point(4,5)
print(p1)
print(p2)
print(p1+p2)