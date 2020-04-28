"""
module usage
"""

#import math4 #ImportError: No module named math4
"""
import math
result=math.sqrt(25)
print "Square root of 25 = ",result
"""

#OR

"""
from math import * #imports all files
result=sqrt(25)
print "Square root of 25 = ",result
"""

from math import sqrt #only imports sqrt
result=sqrt(25)
print "Square root of 25 = ",result
#print pi #NameError: name 'pi' is not defined

num1=9
print "Square of 9 = ",num1**2

num1=10
num2=100
print num1<>num2 #not equal to or diamond operators

print "-"*40

s1="Hello"
print s1*3

