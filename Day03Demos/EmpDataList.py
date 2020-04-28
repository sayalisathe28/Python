"""
Dictionary with diff types of values
"""

emp={'1a':["ABC",25,25000], '2a':["XYZ",35,35000]}  #In memory data storage
print "Emp List Data = ",emp
print "Details of 1a = ",emp['1a']

if type(emp['1a']==list):
    print "Salary of 1a = ",emp['1a'][-1]
    emp['1a'][-1] += 10000
    
print "Salary of 1a after increment = ",emp['1a'][-1]
print "Updated Emp Data = ",emp
print "==============================================="

#2) dict with value as Dict
emp = {'1a':{"Name":"ABC","Age":25,"Salary":25000},'2a':{"Name":"XYZ","Age":21,"Salary":35000}}
print "Emp Dictionary Data= ",emp
print "Emp 2a details = ",emp['2a']
print "Age of 1a = ",emp['1a']['Age']

#CountryData={'English':[]}
