
#OOPDemo9_special_method.py
class oPair:    # ordered pair
    def __init__(self, obj1, obj2):  # constructor
        self.data = (obj1, obj2)     # assign attribute

   
    def __str__(self):   	    # str() string representation
        return str(self.data) 	    # convert tuple to string


    __repr__ = __str__ 		    # repr() string representation
    #special method implementation
    def __add__(self, other):       # add two oPair objects, overriding of +
        return self.__class__(self.data[0] + other.data[0],self.data[1] + other.data[1])
        
                
  
#-------------------------------------------------
#myPair = oPair(6, -4) 	# create instance
#print "myPair = ", myPair   #calls str()
pair1 = oPair(6, -4)
pair2 = oPair(-5, 9)
print "Pair 1= ",pair1 #<__main__.oPair instance at 0x0405BA08>
print "Pair 2= ",pair2

pair3 = pair1 + pair2
if isinstance(pair3, oPair) :print "YES"
print "Addition = ", pair1 + pair2    #pair1.__add__(pair2)
print "--------------------------------------------"
#print dir(pair1)
#we get the error - TypeError: unsupported operand type(s) for +: 'instance' and 'instance'
#if the function def __add__(self, other): is not implemented






#print "------------------------------------------------"
#print dir(oPair)

print dir(object)


"""

    
        #returning an object of oPair class
        #self.__class__   ---> oPair(1,5)  constructor gets called
        
"""
