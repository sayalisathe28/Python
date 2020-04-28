"""Functions parameneters
Default, non default arguments"""

def addition(num1,num2 = 1):    #num1 is non-default, num2 is default 
    return num1+num2

#def addition(num1=0,num):      #default arg should be sfter non-default for correct
   
print "In main module"
print "addition(100,200) = ",addition(100,200)      #300
print "=========================================="

print "addition(100) and 1 = ",addition(100)        #101
print "=========================================="



#addition()          #TypeError: addition() takes exactly 2 arguments (0 given)
print "END!!!!"
