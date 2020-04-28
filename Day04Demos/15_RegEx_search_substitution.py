

import re

s1="Welcome to PSL, PSL in pune"

result = re.sub("PSL","Persistent",s1)
print "Original String = ",s1
print "Substituted String = ",result
print "======================================"

result2 = re.sub("PSL","Persistent",s1,count=1)
print "Substituted String = ",result2
print "======================================"

s1="Welcome to PSL, PSL in pune. psl"
result3 = re.sub("PSL","Persistent",s1,flags=re.I,count=1)
print "Substituted String = ",result2
print "======================================"
