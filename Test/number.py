import random
random_num= random.randint(1,10)
uuu=input()
correct=False
print(random_num)
while not correct:
    if(guess==random_num):
        print("You got it")
        correct=True
    elif(guess>random_num):
        print("You guess high")
        break
    elif(guess<random_num):
        print("You Guess Less")
        break
    else:
        print("You are Wrong")
        break