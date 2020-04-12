num=11.0
if(num>1):
    for i in range(2,num/2):
        if(num%i==0):
            print(num,"Is not a prime number")
            break
        else:
            print(num,"is a prime number")
else:
    print(num,"Is not a prime number")
