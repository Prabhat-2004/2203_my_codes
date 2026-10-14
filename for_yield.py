def disp():
    print("Task-1")
    yield 10
    print("Task-2")
    yield 20
    print("Task-3")
    yield 30
res = disp()
for i in res:
    print(i)