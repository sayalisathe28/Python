"""import Employee.py   as module file"""
import Employee  #importing a file Employee.py
print "*****************************************************"
#further content of Employee file has to be resolved over filename.content
#Employee.Employee
print  "Class level variable = ",Employee.Employee.count

e1 = Employee.Employee("ABC",'1a',25000) #class name referred as function call,
            #will transfer the control to the Default constructor of Employee
            #i.e __init__
print "Object e1 = ", e1 #<__main__.Employee instance at 0x03D3B828>
print "Name of e1 object = ", e1.name
e1.printEmployeeData()#e1 invoking object is passed as implicit parameter
print "-------------------------------------------------------------------"
e2 = Employee.Employee("XYZ", '2a', 45000)
e2.printEmployeeData()
print "-------------------------------------------------------------------"

e3 = Employee.Employee()
e3.printEmployeeData("Employee E3 details:",  100,200)
print "-------------------------------------------------------------------"

Employee.Employee.getCount() #"Employee" class name itself is passed as first implicit parameter
print "-------------------------------------------------------------------"
#class method
Employee.Employee.Emplist = [e1,e2,e3]
totalSalary1 = Employee.Employee.totalSal()
print "totalSalary1 = ",totalSalary1
print "END!!!"























