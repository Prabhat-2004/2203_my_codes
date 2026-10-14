def disp():
    print("Start")
    yield 10
    print("Task1")
    yield 20
    print("Task2")
    yield 30
res = disp()
print(res)


for i in res:
    try:
        print(i)
    except:
        print("No Next Value Is available.")

'''print(res.__next__())
print(res.__next__())
print(res.__next__())
#print(res.__next__()) #StopIteration'''

'''for i in res:
    print(i)'''

'''for i in res:
    try:
        print(res.__next__())
    except:
        print("No Next Value Is available.")'''