
#OOPDemo5_Inheritance1
# parent class

class Parent:
    '''Parent class , super class, base class'''
    def __init__(self):
        print 'created an instance of', self.__class__.__name__   #pre defined attributes
# child class
class Child(Parent):                    # Child inheriting from Parent
    pass
#--------------------------------------------------------------------------
# parent instance
p = Parent()
print "class that got created=",p.__class__ #class that got created above __main__.Parent
print "parent's parent class(es) if any = ",Parent.__bases__  #tuple ()
print "Parent doc string= ",Parent.__doc__
print "Parent class atrributes = ",dir(Parent)
print "-----------------------------------------------------"
# child instance
c = Child()
print "child class that got created=",c.__class__
print "child's parent class(es) = ",Child.__bases__ #(<class __main__.Parent at 0x03EF4AB0>,)
print "child class attributes = ", dir(Child) 

#t1 = (None,)  #ideal def of an empty tuple

