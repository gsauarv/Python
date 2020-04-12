firstNum =int(input("Enter First Number"))
secNum = int(input("Enter Second Number"))
thirdNum = int(input("Enter Last Number"))
if(firstNum==secNum==thirdNum):
    print("All the Number are equal")
else:
    if(firstNum>secNum and firstNum>thirdNum):
        print("The Largest Number is :",firstNum)
    elif(secNum>firstNum and secNum>thirdNum):
        print("The largest Number is ",secNum)
    else:
        print("The Largest Number is",thirdNum)

