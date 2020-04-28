
"""
s="ABC:XYZlmn:pqr"
"""
import re

s1="str1:str2:str3"
list1=re.split(":",s1)  #split function returns a list ['str1', 'str2', 'str3']
print list1
print len(list1)    #3
print "-------------------------------------"

s1="str1:str2*str3?str4"
list1=re.split("[*?:]",s1)
print list1
print len(list1)    #4
print "-------------------------------------"

#split by 'and' or 'or'
s1="my name is sayali and i live in kop"
list1=re.split("and|or",s1)
print list1
print len(list1)    #2
print "-------------------------------------"

#split by : ; , ---
s1="my:name:is;sayali,and---live"
list1=re.split("[:;,]|-{3}",s1)
print list1
print len(list1)    #6
print "-------------------------------------"

#OR
#split by : ; , ---
s1="my:name:is;sayali,and---live"
list1=re.split(":|;|,|-{3}",s1)
print list1
print len(list1)    #6
print "-------------------------------------"

#OR
#split by : ; , ---
s1="my:name:is;sayali,and---live"
list1=re.split("[:;,]|---",s1)
print list1
print len(list1)    #6
print "-------------------------------------"
