
     #try-except statement
def reading():
    #f = open('data11111.txt')     #default read mode   a = IOError()try:
    #above RHS statement raised an object of IOError, object transfers the
    #control to python interporter, error described/prnted and then
    #program halts.
    try:
        f = open('data111.txt')     #default read mode
        print "In try1"
        print "in try 2nd st...."
    
    except IOError as a:       #a = IOError()
        print 'could not open file =', a    #exception handler code
    


        
            
print "Learning Exception Handling......"
reading()     #calling a function
print "END!!!!!"













"""
Learning Exception Handling......
could not open file = [Errno 2] No such file or directory: 'data111.txt'
END!!!!!
"""












"""
try:
        f = open('data.txt')     #default read mode
    except IOError as a:
        print 'could not open file =', a    #exception handler code
"""
