
class oPair:
    def __init__(self,obj1,obj2):   #constructor
        self.data=(obj1,obj2)       #assign attribute , data is tuple

    #overriding instance method
    def __str__(self):              #predefined function of python, we are overriding
        return str(self.data)

    __repr__=__str__

    def __add__(self,other):        #special method (mul,div)
        
        n1=self.data[0] + other.data[0]
        n2=self.data[1] + other.data[1]
        #return (n1,n2) #(1,5) #it returns a tuple
        return self.__class__(n1,n2)    #it returns a oPair()
#--------------------------------------------------

pair1 = oPair(6,-4)
pair2 = oPair(-5,9)
print "Pair1 = ",pair1    #(6,-4) bcz str is there else <something like this will be printed>
print "Pair1 = ",pair2    #(-5,9)

pair3 = pair1 + pair2

if isinstance(pair3,oPair) : print "YES"    #checks that pair3 is of opair type

#print "Addition = ",pair3
#OR
print "Addition = ",pair1 + pair2 #pair1.__add__(pair2)
print "===================================================="

