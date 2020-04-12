def compoundInterest(p,t,r):
    CI=p*(pow((1+r/100),t))
    print("Compound Interest is ",CI)
p=float(input("Enter Principal"))
t=float(input("Enter Time"))
r=float(input("Enter Rate"))
compoundInterest(p,t,r)