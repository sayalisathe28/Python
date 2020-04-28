"""lamba keyword to define anonymous function
function code block loaded in the memory but without any name
"""

def true():     #for this function def, memory is allocated
    return 1

print true()    #calling the function
print "========================================="


ref1 = lambda: 1       #allocate a memory like a function code block nut without any name
#ref1 is a lambda expresion/memory object
print "ref1 = ",ref1   #<function <lambda> at 0x03209130>

#let's call that lambda function
print "return value of lambda call = ",ref1()

print "========================================="

print "return value of lambda call = ",(lambda: 101)() #def and call in one line
print "========================================="

#parametrized lambda
ref1 = lambda num: num**2
print "ref1(2) = ",ref1(2)
#OR
print "Anonymous call = ",(lambda num: num**2)(3)
