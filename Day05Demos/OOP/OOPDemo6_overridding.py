
#OOPDemo6_overridding.py

# parent class
class Parent:
    'Parent class'
    def __init__(self):
        print 'Parent created an instance of', self.__class__.__name__
    def greet(self):
        print 'Hi, I am Parent-greet()'
# child class
class Child(Parent):
    def __init__(self):
        print 'Child created an instance of', self.__class__.__name__
    
    def greet(self):    #over ridding method
        print 'Hi, I am Child-greet()'
        #Parent.greet(self)
#--------------------------------------------------------------------------
p = Parent()
p.greet()
print "------------------------------------------"
c= Child()  # c is an instance of subclass Child
c.greet()
print "------------------------------------------"
#Parent.greet() TypeError
Parent.greet(c)

#subclass  call a base
#class method which is
#overridden in the subclass 
#Parent.greet()   run time error as TypeError unbound


























































