def reading():

    #f=open('data111.txt')   #default read mode - IOError

    try:
        f=open('data111.txt')
    except IOError as a:
        print "could not open file = ",a  #exception handler code

print "Learning Exception Handling"
reading()
print "END!!!!"
