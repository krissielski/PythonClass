#Lesson14 - Advanced Topics

# Python GUI:  Tkinter

#Formatted Prints:
val1 = 'Python'
val2 = 1337

#standard:
print( "The", val1, "langauge is", val2 )

#f-string
print( f"The {val1} langauge is {val2}" )

#format
print( "The {} langauge is {}".format(val1,val2) )

#C++ like % operator
print( "The %s langauge is %d" %(val1,val2) )


#Enumerate
mylist = ['A','B','C','D']

for index in range(len(mylist)):
    print(index, mylist[index])

print("***********")

for letter in mylist:
    print(letter)

print("***********")

for index,letter in enumerate(mylist):
    print(index,letter)


print("********************************")

print( enumerate(mylist))



