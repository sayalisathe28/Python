
class oPair:
    def __init__(self,obj1,obj2):   #constructor
        self.data=(obj1,obj2)       #assign attribute , data is tuple

    #overriding instance method
    def __str__(self):              #predefined function of python, we are overriding
        return str(self.data)

    #__repr__=__str__
    #OR
    def __repr__(self):
        return str(self.data)

#--------------------------------------------------

myPair = oPair(6,-4)        #create instance
print "myPair = ",myPair    #calls myPair.__str__() default function 
