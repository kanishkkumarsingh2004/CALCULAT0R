A = input ("Enter your first number : ")
B = input ("Enter the operation (+,-,*,/,%) :")
C = input ("Enter your second number : ")
A = int(A)
C = int(C)
if B == "+":
    print (A + C)
elif B == "-":
    print (A - B)
elif B == "*":
    print (A * B)
elif B == "/":
    print (A / B)
elif B == "%":
    print (A % B)    
else:
    print ("invalid operation")