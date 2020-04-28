class Employee:

    
    def __init__(self,n="",sal=0.0):
  
        self.name=n
        self.salary=sal
        #Employee.empList.append([self.name,self.salary])
   
    def displayEmployee(self):
        print "Employee Details......."
        print "Name = ",self.name
        print "Salary = ",self.salary


print "Enter Employee(s) Name and Salary"
empList=[]
while True:
    input1=raw_input()
    if input1=="": break
    data=input1.split(" ")
    empList.append(data)
    

for i in range(len(empList)):
    obj1=Employee(empList[i][0],empList[i][1])
    obj1.displayEmployee()
    print "=========================================="




