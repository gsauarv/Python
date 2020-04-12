print("hello")
import random
random_num= random.randrange(1,10)
guess=int(input("Enter a number"))
correct=False
print(random_num)


while correct==False:
    if guess==random_num:
        print("You got it")
        correct=True
    elif guess>random_num:
        print("You guess high")
        break

    elif guess<random_num:
        print("You Guess Less")
        break
    else:
        print("You are Wrong")
        break