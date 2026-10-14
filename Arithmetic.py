num1 = int(input('Enter num 1 : '))
num2 = int(input('Enter num 2 : '))
choose = input("Enter Add = 1, Sub = 2, Mul = 3 , Div = 4 , PowerSquare = 5 , FloarDevision = 6 & Modulus = 7 : ")

if choose == '1':
    print(f"Addition of '{num1} + {num2}' is : {num1 + num2}")
elif choose == '2':
    print(f"Substraction of '{num1} - {num2}' is : {num1 - num2}")
elif choose == '3':
    print(f"Multiplication of '{num1} * {num2}' is : {num1 * num2}")
elif choose == '4':
    print(f"Division of '{num1} / {num2}' is : {num1 / num2}")
elif choose == '5':
    print(f"PowerSquare of '{num1} ** {num2}' is : {num1 ** num2}")
elif choose == '6':
    print(f"FloarDivision of '{num1} // {num2}' is : {num1 // num2}")
elif choose == '7':
    print(f"Division of '{num1} % {num2}' is : {num1 % num2}")
else :
    print(f"Invalid Choose")