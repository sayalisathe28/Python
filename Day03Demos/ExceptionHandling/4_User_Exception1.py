
#creating a sub class
#Exception is pre defined class, create user defined class MYError as subclass of Exception
# in java ----> class AgeError extends Exception{}

class MyError(Exception):   #inheritance, superclass is Exception, MyError is subclass
    pass
     
#-------------------------------------------------------------
b1 = MyError()   #create an object 
#print "Object b1 = ", b1 #<__main__.MyError instance at 0x035103A0>

#raise MyError("Some information about what went wrong")#calling a constructor

try:
    age = 15
    if age <18:
        raise MyError("Some information about what went wrong")

except MyError as error:
    print("Situation:", error)


print "Prgrom proceeds............."





















"""
try:
    
    raise MyError("Some information about what went wrong")

except MyError as error:
    print("Situation:", error)
"""


"""

class Employee:       18    to 50  

    
class AgeError(Exception):
    pass

if (age<18 or age>50):
    raise AgeError("")
    
"""
