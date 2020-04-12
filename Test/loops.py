num = int(input("Enter a num"))
fac=1
if(num<0):
    print("Sorry")
elif num==0:
    print("Factorial is 1")
else:
    for i in range(1,num+1):
        fac=fac*i
    print("Factoriall is ",fac)
