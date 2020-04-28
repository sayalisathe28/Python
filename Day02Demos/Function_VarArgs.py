"""Variable no of arguments capturing facility:
2 ways:-
1. special catching argumnet named as tuple: *theVar or *x, *y
    *theVar which is tuple can capture only non-keyword parameters passes
2. special catching argumnet named as dictionary: **theVar or **x, **y

"""

def display(arg1,arg2=1, *theRest):
    print "arg1 = ",arg1
    print "arg21 = ",arg2
    print "theRest tuple var = ",theRest

print "In main module...."
#display()  #TypeError: display() takes at least 1 argument (0 given)
display(99)
print "============================="
display(99,"abc",55,66,77)      #theRest=(55, 66, 77)
print "============================="
display(99,"abc",[55,66,77])    #theRest= ([55,66,77],) ->tuple of 1 list
    
print "============================="
#display(99,"abc",x=66,y=55)     #TypeError: display() got an unexpected keyword argument 'x'
