"""
OOP: 3 pillers : Class, object creation , calling a method over an object
how to achieve Overloading : same method name in diff signatures form
"""

class Employee:
    def __init__(self,n1="NIL",id1="100A",sal1=20000): #constructor function
        print "In init, self = ", self #<__main__.Employee instance at 0x03DC03A0>
        self.empId = id1
        self.name = n1
        self.sal = sal1
    
    def printEmployeeData(self, msg= "Emp Details......", *theRest):   #instance / data member method
        print msg
        print "Name of emp = ", self.name
        print "ID of emp = ", self.empId
        print "Sal of emp = ", self.sal
        
        
#main program
#instantiate this class
e1 = Employee("ABC",'1a',25000) #class name referred as function call,
            #will transfer the control to the Default constructor of Employee
            #i.e __init__
print "Object e1 = ", e1 #<__main__.Employee instance at 0x03D3B828>
print "Name of e1 object = ", e1.name
e1.printEmployeeData()#e1 invoking object is passed as implicit parameter
print "-------------------------------------------------------------------"
e2 = Employee("XYZ", '2a', 45000)
e2.printEmployeeData()
print "-------------------------------------------------------------------"

e3 = Employee()
e3.printEmployeeData("Employee E3 details:")
print "-------------------------------------------------------------------"








