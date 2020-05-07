#Lesson12 - Exceptions

from time import sleep

# try:
#   < code that might have an error >
#
# except < Type?? >:
#   <Handler, recovery>

##
##
##while( True ):
##
##    try:
##        sleep(0.1)
##        pass
##    except KeyboardInterrupt:
##        print("Exception!!!!")
##        break
##    except:
##        print("Default exception")
##        break
##
##
##
##print("Done")
##

while(True):

    try:
        age = eval(input("What is your age: ") )

        print("Your Age:", age)
        break
    except KeyboardInterrupt:
        print(" Ctrl-C Pressed")
        break

    except NameError:
        print("That is not a number!!")
    


print("Done")
