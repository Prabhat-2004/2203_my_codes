# Python don't support method overloading...
def disp():
    print("Inside in o argument..")
def disp(a):
    print("Inside in 1 argument..")
def disp(a,b):
    print("Inside in 2 argument..")
def disp(a,b,c):
    print("Inside in 3 argument..")

#disp()    #disp() missing 3 required positional arguments: 'a', 'b', and 'c'
#disp(1)    #disp() missing 2 required positional arguments: 'b' and 'c'
#disp(1,2)   #disp() missing 1 required positional argument: 'c'
disp(1,2,3) #Inside in 3 argument..
