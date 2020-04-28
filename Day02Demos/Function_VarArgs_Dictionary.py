"""Variable no of arguments capturing facility:
2 ways:-
2. special catching argumnet named as dictionary: **theVar or **x, **y
    **theRest is a special dictionary
    capable od capturing any excessive keyword argument passed
"""
#def display(arg1,**theRest,arg2=1): #SyntaxError
def display(arg1,arg2=1, **theRest):
    print "arg1 = ",arg1
    print "arg21 = ",arg2
    print "theRest tuple var = ",theRest

print "In main module...."
display(99)
print "============================="
display(99,"abc",x=66,y=55)
print "============================="
#display(99,"abc",55,66,77)      #TypeError: display() takes at most 2 arguments (5 given)
#display(99,"abc",[55,66,77])    #TypeError: display() takes at most 2 arguments (3 given)
    
display(99,"abc",x=66,y=55)    # **theRest takes only keyword argument
