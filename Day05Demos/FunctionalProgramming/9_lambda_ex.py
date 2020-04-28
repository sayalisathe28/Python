

#9_lambda_ex.py
def true():         #just a sample function def
    return 1
print true()    #calling true() named function and then printing it's return value

print "----------------------------------------------------"
#anonymous function in Python by lambda
print lambda:1  #this loads  a function without any name anonymous  , after : is the return value
#<function <lambda> at 0x03E6FAF0>
print "----------------------------------------------------"

a= lambda:1
print a
print a()    #function getting called\
print "----------------------------------------------------"


ref1 = lambda num : num**2  #num is catching argument of lambda function
print "Square of 5 = ", ref1(5)  #calling/invoking a lambda function


print "Persistent in Uppercase =",(lambda str1 : str1.upper())("Persistent")
#(lambda str1 : str1.upper())  this allocates a memory as function
#(lambda str1 : str1.upper())("Persistent")  this call that lambda function






"""
def squarefunc(num):
    return num**2

print "Square of 5 = ", squarefunc(5)

print "----------------------------------------------------"

                #as an alternative let's write lambda

b = lambda num : num**2
print "b = ", b
result = b(6)
print "Square of 6 = ", result
print "----------------------------------------------------"
"""









"""
Assignment
str1 = "persistent"
convert a given string into uppercase, write lambda for this

str1 = "persistent"
ref1 = lambda stringVar : stringVar.upper()      #anonymous func written using lambda
print "Upper o/p = ", ref1(str1)
print "----------------------------------------------------"

print (lambda stringVar : stringVar.upper())("abc") #anonymous func written using lambda and called it

"""



































