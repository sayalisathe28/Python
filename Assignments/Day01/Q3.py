class Employee:

    empCount=0
    empList=[]
    def __init__(self,n="",sal=0.0):
        Employee.empCount += 1
        self.name=n
        self.salary=sal
        Employee.empList.append([self.name,self.salary])
        
    def displayCount(self):
        return Employee.empCount

    @staticmethod
    def displayEmployee():
        print "Employee Details......."
        print Employee.empList


obj1=Employee("Sayali",25000)
obj2=Employee("Sakshi",35000)

Employee.displayEmployee()
print "=========================================="

print"Total no of Employees are = ",Employee.empCount
