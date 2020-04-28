""" My final application :use user defined modules """
import mymath   #import creates mymath.pyc and module name of mymath chnages from main to mymath
print "********************************************************"

print "area of circle with radius 2 = ",mymath.area(2)
#fib(21) #NameError: name 'fib' is not defined
mymath.fib(21)
