def add(a,b):
   print("Starting Program..")
   return a/b

try:
    x = add(10,0)
    print(x)
except:
    print("Exception handling occurs...")
else:
    print("Exceptionn handling is not here...")
finally:
    print("Program is end...")
print("Other task can start...")
