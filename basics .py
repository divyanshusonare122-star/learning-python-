#comparision operator return boolean values <= , >= , = , > , < , !=
s = 5>=7
print(s)
r = 10 
t = r != 20
print(t)
e = 5==5
print(e)

#assignment operator *= , += , /= , -= , %=
b=4
b+=5 #increament the value of b by 5 and then assign it to b
b*=3
print(b)

#logical operator

True or False

print("True or True  ",True or True )
print("True or False ",True or False )
print("False or True ",False or True )
print("False or False",False or False )


True and False


print("True or True  ",True  and True )
print("True or False ",True  and False )
print("False or True ",False and True )
print("False or False",False and False )

# multi cursor functionality of vscode use  Alt + click on the place you want to add the cursor

#shif + enter = run the particult line of the cursor

#not operator
print(not(False))

# In Python, the type() function is used to identify or check
# the data type of a variable 

a = "31.4"
b = type(a)
print(b)


# by using type function we can change the type of the particular variable
# int()
# float()
# str()
# bool


s = 6.6
t = int(s)
print(t)
print(type(t))
e = bool(t)
print(e)

# we have to mention the type while defining the variable 
# other wise it takes sting
a = int(input("enter the number "))
b = int(input("enter the number "))
c = a+b
print(f"the value of {a} + {b} is {a+b}") 
print(c)



