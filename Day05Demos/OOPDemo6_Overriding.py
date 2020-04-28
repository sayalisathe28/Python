
class Parent:
    '''parent class, super class, base class'''
    
    def __init__(self):
        print"Parent created an instance of ",self.__class__.__name__  #predefined

    def greet(self):
        print "Hi. I am Parent-Greet"

        
class Child(Parent):    #class inheriting from Parent
    def __init__(self):
        print"Child created an instance of ",self.__class__.__name__  #predefined

    def greet(self):    #overriding method
        print "Hi. I am Child-Greet"
        #Parent.greet(self) #like super()

p=Parent()
p.greet()       #Parent-Greet
print "============================================="
c=Child()
c.greet()       #Child-Greet
print "=============================================="
Parent.greet(c) #Parent-Greet
