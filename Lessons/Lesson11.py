#Lesson10 - Files

#process:
#   Open file
#   read or write
#   Close

#Open

# <varName> = open( <filename>, <mode> )  

#  'r' = open for reading (default)
#  'w' = open for writing, truncating the file first
#  'a' = open for writing, appending to the end of the file if it exists
#-Modifiers-
#  'b' = binary mode
#  't' = text mode (default)
#  '+' = open for updating (reading and writing)

openfile = open("./Lessons/Kris.txt", 'w' )

openfile.write("Hello Kris!!!\n")

openfile.write("Hello Class!!!\n")
openfile.write("This is line 3")

openfile.flush()
openfile.close()


#Reading from a file

# read(#)    - Read # of characters
# read()     - Read whole file
# readline() - Read next line


openfile = open("./Lessons/text.txt")

#data = openfile.read(10)
data = openfile.readline()

print (data)

openfile.close()




