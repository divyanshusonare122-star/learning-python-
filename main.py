name = 'hellow' 
## strings are immutable

##Indexing in programing language stars from 0th index
#0123456789
# h e ll ow

#if move in reverse order the index become -1
#      ..-1
# h e ll ow

#lenght of the string = number of character in the string
name = "hellow"
#lenght = 6
#len()
name = "divyanshu"
print(len(name))

## string slicing
# print till 0 to n-1 
variable_1 = "hellow-divyanshu"

var_2 = variable_1[0:4] 
print(var_2)
var_3 = variable_1[-4:-1]
print(var_3)

# name[x : y]
#if in the place of x nothing mention then it is 0   [0: ]
#same if place of y noting mention then it is lenght [:lenght]

bro = "sonare"
hi = bro[0:]
print(hi)



## string function

name = 'narendra modi'
print(name.startswith("nar"))
print(name.endswith("modi"))
print(name.capitalize())
print(name.title())
print(name.upper())
print(name.lower())
print(name.swapcase()) #lower to upper and vice versa

a = "harry is good good boy"
b = a.replace("good","bad")
print(b)

# It replace all the occurances of a string
  

#Escape sequence character
#\n new line
a = 'harry is a good\n boy not \na bad boy'
print(a)

#\t
print("Rahul\t20\tIndore")
print("Dakshu\t20\trajendranagar")

#\\ backslash
name = input("Enter you name: ")
print(f"hellow\\{name}")

#Single Quote (\')
print("it\'s dakshu phone")

#Double quote (\")
print("hellow dad \"its my new car\"")







#shortcut 
#by using (Alt + ) we can move the particular line of code