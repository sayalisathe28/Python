nums = [1,2,3,4,5]

# 1) list comprehension
square_elements = [i**2 for i in nums]
print "Original nums list = ",nums
print "Square elements = ",square_elements
print "----------------------------------------------------"

# 2) alternative solution : map() function call
def squareElement(x):
    return x**2

#print "squareElement(5) = ",squareElement(5)

square_elements2 = map(squareElement,nums)  #returns list/ returns map object 
print "Square elements = ",square_elements2
print "----------------------------------------------------"

#In Python 3
"""
mapObj = map(squareElement,nums) #returns map object
newList = list(mapObj)

"""

# 3) alternative solution : map() function call with lambda

#Basics
"""
ref1 = lambda x: x**2
print ref1(3)
#or
print "Return of lamda = ",(lambda x: x**2)(5)
"""

square_elements3 = map(lambda x: x**2,nums)
print "Square elements = ",square_elements3
print "----------------------------------------------------"

"""
words = ["abc","xyz"]
covert all elements from words in upper case
upperwords =[]
1. by using map and lambda
"""
