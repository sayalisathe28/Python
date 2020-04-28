

def display(arg1,arg2=1, *x,**theRest):
    print "arg1 = ",arg1
    print "arg21 = ",arg2
    print "x tuple var = ",x
    print "theRest dict var = ",theRest

print "In main module...."
display(99)
print "============================="
display(99,"abc",x=66,y=55)
print "============================="
display(99,"abc",55,66,77)      
#display(99,"abc",[55,66,77])    #TypeError: display() takes at most 2 arguments (3 given)
print "============================="
emp={'1a':200,'2a':300}
display(99,"abc",emp)       #emp content will get stored in *x
print "============================="
display(99,"abc",**emp)     #emp content will get stored in **theRest
