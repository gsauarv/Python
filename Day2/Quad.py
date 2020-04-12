import math
a = float(input("Enter the value of a"))
if(a>0):
    b= float(input("Enter the value of b"))
    c=float(input("Enter the value of c"))
    Uroot = (b*b)-(4*a*c)
    x1= (-b+math.sqrt(Uroot))/(2*a)
    x2 = (-b-math.sqrt(Uroot))/(2*a)
    print("The value of x1 and x2 is:")
    print(x1,x2);
else:
    print("The Value of a should be Greater then 0 to be Quadradic Equation")
