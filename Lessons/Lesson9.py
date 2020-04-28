#Lesson9 - Lists and Touples

#list = []
#touple = ()

numlist = [ 3,8,1,4,2,5,7,6]
numlist.sort()


#Adding to list
numlist.append( 9 ) 

#Removing from list
#remove
#  .pop()       <<< From End
#  .pop(index)  <<< From Index # (0=beginning)
#  .remove( value )

#Other functions used on lists
# max()
# min()
# sum()


#iterating

#Noob:
for i in range (len(numlist)):
    print( numlist[i])

#Pro:
for num in numlist :
    print( num )


#Define a touple
days = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat')

###  [] brackets on touple!!!!
print(  days[1] )

## Why Touples over lists?
    # Read Only, 
    # passing data,  
    # data integrity, 
    # storage efficiency






