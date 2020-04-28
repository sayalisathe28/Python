"""
OOP: Class level variable : static var cancept

"""

class Employee:
    """Overloading concept """
    count =0    #class level variable
    Emplist = []  #class level variable - list
    def __init__(self,n1="NIL",id1="100A",sal1=20000): #constructor function
        print "In init, self = ", self #<__main__.Employee instance at 0x03DC03A0>
        self.empId = id1
        self.name = n1
        self.sal = sal1
        Employee.count += 1
    
    def printEmployeeData(self, msg= "Emp Details......", *theRest):   #instance / data member method
        print msg
        print "Name of emp = ", self.name
        print "ID of emp = ", self.empId
        print "Sal of emp = ", self.sal

    @staticmethod
    def getCount():   
        print "Count of Employee objects = ", Employee.count
        

    @classmethod
    def totalSal(cls):    #cls = Employee
        print "In totalSal method, Count = ",cls.count
        #print "Sal = ", self.sal#NameError: global name 'self' is not defined
        totalSalary = 0
        for e in cls.Emplist:  #e is one Employee object
            totalSalary += e.sal
        
        return totalSalary
    
        
#---------------------------------------------------------------------------------       
#main program
#instantiate this class
print  "Class level variable = ",Employee.count

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
e3.printEmployeeData("Employee E3 details:",  100,200)
print "-------------------------------------------------------------------"

Employee.getCount() #"Employee" class name itself is passed as first implicit parameter
print "-------------------------------------------------------------------"
#class method
Employee.Emplist = [e1,e2,e3]
totalSalary1 = Employee.totalSal()
print "totalSalary1 = ",totalSalary1
print "END!!!"























