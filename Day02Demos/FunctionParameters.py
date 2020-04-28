"""Functions parameneters
psitional arguments"""

def  display():                         #function definition
    print "In display function...."

def addition(num1,num2):
    return num1+num2

def listfun(newlist):                   #newlist=list1 //shallow copy
    print "newList = ",newlist
    print "Id of newList = ",id(newlist)
    newlist.append([11,22])
    
print "In main module"
display()                               #calling/invoking funcion
#display2()                             #NameError: name 'display2' is not defined

print"================================="
print display()                         #In dsipaly function....None
print"================================="

print "addition(100,200) = ",addition(100,200)
print"================================="

list1=[1,2,3,4]
print "Id of list1 = ",id(list1)
#listfun()                              #TypeError: listfun() takes exactly 1 argument (0 given)
"""
listfun(list1)              #original list gets modified
print "after listfun call list1 = ",list1
"""
listfun(list1[:])           #original list does not get modified
print "after listfun call list1 = ",list1 


print "END!!!!"
