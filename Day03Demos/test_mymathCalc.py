#if __init__.py is not written - call would be mymath.area(2)

from mymathCalc import *
print "Area of Circle = ",area(2)
fib(31)

print "Addition = ",add(2,3)

#after adding area() in mymath2.py also
#area() is same method in mymath and mymath2 so better user mymath.
print "Area of Circle = ",mymath.area(2)
print "Area of square = ",mymath2.area(2)
