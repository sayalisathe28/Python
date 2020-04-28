
class Parent:
    '''parent class, super class, base class'''
    
    def __init__(self):
        print"created an instance of ",self.__class__.__name__  #predefined

class Child(Parent):    #class inheriting from Parent
    pass

p=Parent()
print "Class that got created = ",p.__class__ #gives class that got created above __main__
print "Parent's parent class(es) if any = ",Parent.__bases__    #tuple()
print "Parent doc string = ",Parent.__doc__
print "Parent class attributes = ",dir(Parent)
print "=================================================="
c=Child()
print "Child clas that got created = ",c.__class__
print "Child's parent class(es) = ",Child.__bases__ #(<class __main__.Parent at 0x02D2C688>,)
print "Child class Attributes = ",dir(Child)
