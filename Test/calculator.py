def add_Num(num1,num2):
    return num1+num2
def sub_Num(num1,num2):
    return num1-num2
def muliply_num(num1,num2):
    return num1*num2
def division_num(num1,num2):
    return num1//num2
num1=int(input("Enter a num"))
num2=int(input("Enter another number"))
select=int(input("Enter 1:Add " + "\t" + "2:Substract" +"\n" + "3:Muliply"+"\n" + "4:Division"))
if(select==1):print("The Sum is: ",add_Num(num1,num2))
elif(select==2):print("The Differences is: ",sub_Num(num1,num2))
elif(select==3):print("The product is: ",muliply_num(num1,num2))
else:print("The Division is: ",division_num(num1,num2)         