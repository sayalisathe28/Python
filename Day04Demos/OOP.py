"""
OOP: Class, Object, instance methods
"""

class SayHello:
    count=0     #class level variable - only one mem is allocated
    def __init__(self,msg="Hello",*x,**y):                  #constructor
        print "Inside init constructor, self = ",self
        self.message=msg    #instance var
        SayHello.count+=1
        message="BYE!!!!"               #This is not instance property

    def display(self):                  #instance method
        print "Inside display method, self = ",self
        print "Message = ",self.message

    #@staticmethod
    def testing():
        print "In testing method....."
        return SayHello.count
        
if __name__ == "__main__":

    #create an object of a class SayHello
    
    obj1=SayHello()#LIKE FUNCTION CALL SYNTAX (it calls __init__() internally
                   # by passing memory reference as impicit paratmeter)

    print "Obj1 = ",obj1 #<__main__.SayHello instance at 0x02D18878>
    #print "obj1.message() = ",obj1.message
    obj1.display()  #calls display() method, by passing obj1 itself as implicit parameter 
    print "==========================================================="

    obj2=SayHello()
    print "Obj2 = ",obj2 #<__main__.SayHello instance at 0x02D18EE0>
    obj2.display()
    print "==========================================================="
    
    obj3=SayHello("Hello Sayali")
    obj3.display()  #calling with parameters - overloading

    print "==========================================================="
    print "Class Level variable = ",SayHello.count
    print "==========================================================="
    print "Class Level variable = ",SayHello.testing() #calling static method
