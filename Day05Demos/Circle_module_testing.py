"""
import Circle #Imports the file

#filename.classname
obj1 = Circle.Circle(5)
print "Area of Circle  = ",obj1.area()
print "=================================="

obj2 = Circle.Circle()
print "Area of Circle  = ",obj2.area()
print "=================================="

print "Total no of Circle objects = ",Circle.Circle().getCount()
"""

#OR

from Circle import *

#access directly by classname
obj1 = Circle(5)
print "Area of Circle  = ",obj1.area()
print "=================================="

obj2 = Circle()
print "Area of Circle  = ",obj2.area()
print "=================================="

print "Total no of Circle objects = ",Circle().getCount()
