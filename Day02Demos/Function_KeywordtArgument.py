"""Functions parameneters
keyword, non-keyword arguments"""

def addition(num1,num2):   
    return num1+num2

   
print "In main module"
print "addition(100,200) = ",addition(num2=100,num1=200)      #300
print "=========================================="

print "addition(1) and num2=20 = ",addition(1,num2=20) #non-keyword,keyword       
print "=========================================="
#addition(num1=9,20) #syntax error : keyword parameter should be last   
print "=========================================="
#addition(9,num1=20)  #TypeError: addition() got multiple values for keyword argument 'num1'
print "=========================================="
#addition()  #TypeError
#addition(1,2,3,4)  #TypeError

