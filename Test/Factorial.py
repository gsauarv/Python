def factorial(num):
    if(num<0):
        return 0
    elif(num==0 or num==1):
        return 1
    else:
        fact =1
        while(num>1):
            fact = fact *num
            num=num-1

        return fact
num=int(input("Enter the Num for the factorial"))
print("Factorial of ",num,"is",factorial(num))  

    