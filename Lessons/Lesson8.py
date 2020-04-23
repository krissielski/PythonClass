#Lesson8 - Lists

# List = []

#Empty list

emptylist = []

#Define a list
days = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']

#Access data with []
#days[2]
#days[1:4]


numlist = [1,2,3,4,5,6,7,8]

wackylist = ["hello", 1, 3.14, True]


#Iterate
for i in range( len( numlist )):
    print( numlist[i] )


#addlist
numlist.append(123)
numlist.insert(3,'hello')

print(numlist)


#Example of List in a list
list1 = days
list1.append(numlist)

print(list1)

