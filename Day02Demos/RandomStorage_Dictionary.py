"""
Random data storage

2.Dictionary
{key:value, key:value}
key : has to be unique - immutable - int float string tuple
va;ue : can be same, anything
refer a key and get its value

Hash table concept
"""

d1={}   #DICTIONARY
print "d1 = ",d1 #{}
print "Type of d1 = ",type(d1)
print "==================================================="

emp={'1a':25000,'2a':30000}
print "Emp Data = ",emp             #Emp Data =  {'1a': 25000, '2a': 30000}
print "Salary of 1a = ",emp['1a']   #Salary of 1a =  25000
emp['3a']=45000                     #creates a ney key value pair
print "Updated emp dict = ",emp     #Updated emp dict =  {'1a': 25000, '3a': 45000, '2a': 30000}

keylist=emp.keys()
print "Keys are = ",keylist
sallist=emp.values()
print "Salaries are = ",sallist
print "Total sal = ",sum(sallist)
print "emp items = ",emp.items()    #returns a list of tuple and tuple= key value pair
print "==================================================="

emp['3a']=55000                     #oveerides a value so check condition
print "Updated emp dict = ",emp
if '1a' not in emp:
    emp['3a']=55000                 #overrides a value 
    print "Updated emp dict = ",emp
print "==================================================="

e1={'5a':95000}
emp.update(e1)                      #add this e1 to emp
print "Updated emp dict after update = ",emp

print "==================================================="
for i in emp:                      
    print "Key = ",i," Value = ",emp[i]
    emp[i]+=10000                   #dict will get updated

print "==================================================="
#emp.keys().sort()
k1=emp.keys()
k1.sort()
print k1
for i in k1:                        #controlled sequence
    print "Key = ",i," Value = ",emp[i]


"""
Assignment

1.Accept Emp data as below key:value per line input till blank entry->
    1a:25000
    2a:35000
    ->
    Hint : while(True):
                input1=raw_input()
                input1=input1.rstrip()
                list1=input1.split(":")
                now create a dict pair out of above list1 content
2.print them in sorted keys manner
3.search for given emp id(raw_input)if it exists print its salary
    (use has_keys or in)
"""

