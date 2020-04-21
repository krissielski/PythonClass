#Lesson7 - Classes III Review

def MyFunc( left, right  ):
    return left + right


class Time:

    def __init__ (self, h, m):
        self.hour   = h
        self.minute = m

    def SetMe(self, h, m ):
        self.hour   = h
        self.minute = m

    def AddTime(self, h, m):
        self.hour  =  self.hour   + h
        self.minute = self.minute + m


    def __str__(self):
        #Must return a string
        return str(self.hour) +  str( self.minute)
    
    def __len__(self):
        #Must return an int
        return self.hour * 60 + self.minute

    def GetMe(self):
        return self.hour

#####  MAIN ######
print("Hello")

myvar = 3.14
print( MyFunc(10 , 20 ) )


t1 = Time( 50, 25)
#t1.SetMe(50,25)

#t2.AddTime( 10, 15)



t2 = Time(1,2)


t2.SetMe(100,150)

t1.GetMe()

mystr = t1 + "dshjsdkfhsdjkf"

len(t1)


print("Done")
