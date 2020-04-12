def printw(s):
    s=s.split(' ')
    for word in s:
        if(len(word)%2==0):
            print(word)

s= "ii am saurav"
printw(s)