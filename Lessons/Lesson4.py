#Lesson4 - Functions

print(" Hello" )

#Function General Form:

##def <func name> (   <param_list> )  :
##    #code
##    #Posible return

def my_function( value ):
    print( value )


def my_func( a,b,c,d ):
    print( a,b,c,d )

    
def my_func2( a,b,c,d ):
    return a+b+c+d

def my_func5( word ):
    if word == "hello":
        return True
    else:
        return False

def find_square( num ):
    squ = num * num
    return squ


##  MAIN ###
my_function(" Dude")

my_func( "hello", 23, 3.13, "dude" )

print( my_func2 ( 1,2,3,4 ) )

print( my_func5("hello") )

print( find_square( 5 ) )


