import MySQLdb  #this is not a part of standard Python library set
# Open database connection handle
db = MySQLdb.connect("localhost","root","root","assignment2" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
# Drop table if it already exist using execute() method.
#cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# Create table as per requirement
"""sql = CREATE TABLE EMPLOYEE (
         NAME  CHAR(20) NOT NULL,
         EMPID INT,
         AGE INT,  
         SAL FLOAT ) #multiline string

cursor.execute(sql)

"""
name="swagata"
empid=1
age=22
sal=30000

class Employee:
    def __init__(self,name,empid,age,sal):
        self.name=name
        self.empid=empid
        self.age=age
        self.sal=sal
    def show(self):
        print "Employee details: "
        print self.name
        print self.empid
        print self.age
        print self.sal

emp1=Employee(name,empid,age,sal)
emp1.show()


sql="""INSERT INTO EMPLOYEE VALUES('%s', '%d', '%d', '%f' )""" % (emp1.name,emp1.empid,emp1.age,emp1.sal,)
cursor.execute(sql)
db.commit()
print cursor.fetchall()




res="""SELECT * FROM EMPLOYEE"""
cursor.execute(res)
print cursor.fetchall()

#disconnect from server
db.close()
