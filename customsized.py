'''class Custmized(Exception):
    pass
def sub(a):
    if a > 0:
        raise Custmized("Number is gaater than >>> 0")
try:
    sub(10)
except:
    print("Number is grater than zero...")'''

def calculate_sqr_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number..")
    return x ** 0.5
try:
    result = calculate_sqr_root(4)
    print(f"Result: {int(result)}")
except ValueError as e:
    print(e)