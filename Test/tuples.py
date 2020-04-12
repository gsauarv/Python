#tuples are immutable python objects.
Fruits = ("Mango","Apples","Grapes")
Veggies = ("Tomato","Raddish","Sweets")
#indexing
print(Fruits[1])
print(Fruits.index("Mango"))

#slicing
print(Fruits[0:2])
print(Fruits[::-1])
#concat
fru=Fruits+Veggies
print(fru)

#Repetaiton
print(Fruits*2)
print(Fruits.count("Mango"))
print(Fruits.__len__())


