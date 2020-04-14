#Lesson5 - Classes

#Visual Studio Code
#------------------
# Download from Ninite.com
# Extentions:  Install  Python
#   Should ask to install PyLint:  YES!
#

#Options:  Ctrl-Shift-P


 #WHY use classes?
 #  Code Organization
 #  Modularity
 #  Breaking down problem into simpiest form.
 #  Advanced Topics: NOT THIS COURSE
 #     Inheritance
 #     Polymorphism


class Time:

    def __init__(self):

        #Attributes
        self.hour   = 0
        self.minute = 0
        self.second = 0

    #Class Method
    def SetTime(self, h,m,s ):

        self.hour   = h
        self.second = s
        self.minute = m

    def PrintTime(self):
        print("The time is: ", self.hour,":", self.minute,":",self.second )



#####  MAIN ######
timer1 = Time()
timer2 = Time()

timer1.SetTime(1,2,3)
timer2.SetTime(5,6,7)

timer1.PrintTime()
timer2.PrintTime()



#Homework:
# Write a Class "Student" with Attributes of Name, Grade, GPA
# Instanciate objects for each student in this class, assign values to attribues ("Setter Function")
#  Then print each student object to console






