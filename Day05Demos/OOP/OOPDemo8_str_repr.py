
#OOPDemo8_str_repr.py
class oPair:    # ordered pair
    def __init__(self, obj1, obj2):  # constructor
        self.data = (obj1, obj2)     # assign attribute , data is a tuple (6, -4)

    def __str__(self):              #pre defined function of Python, we are overriding
        return str(self.data)
    __repr__ = __str__
#-------------------------------------------------
    
       
myPair = oPair(6, -4) 	# create instance
print "myPair = ", myPair   #calls __str__() default function for default string representation


















"""
#myPair.__str__()when object is printed within a file


#default str presenataion is <__main__.oPair instance at 0x0000000002F62108>
myPair2 = oPair(10,20)
print "myPair2 = ", myPair2

#if oPair class object is referred outside this file (on shell prompt or
#in another file)
#ob1.__repr__() is called






"""





"""
def __str__(self):# str() string representation
        return str(self.data) 	        # convert tuple to string

    __repr__ = __str__ 		# repr() string representation  outside this current module

    

"""























