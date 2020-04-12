def reverse(s):
    return s[::-1]
def ispalindrome(s):
    rev =reverse(s)
    if(s==rev):
        return True
    else:
        return False
s=input("Enter a word")
ans = ispalindrome(s)
if(ans==1):
    print("Yes")
else:
    print("No")