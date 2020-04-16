
class Time:

    def __init__(self,h=20,m=15,s=10):

        #Attributes
        self.hour   = h
        self.minute = m
        self.second = s


    #dunders/Magic methods
    #__len__
    #__str__

    def __str__(self):
        #return( "Hello!!!!!") 
        return "The time is: " + str(self.hour)+" : "+str(self.minute)+":"+str(self.second)

    def __len__(self):
        return self.hour  


    #Class Method
    def SetTime(self, h,m,s ):

        self.hour   = h
        self.minute = m
        self.second = s

    def SetHour(self,h):
        self.hour = h

    def PrintTime(self):
        print("The time is: ", self.hour,":", self.minute,":",self.second )

