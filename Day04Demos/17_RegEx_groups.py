
"""
s="ABC:XYZlmn:pqr"
"""
import re

s1="Oct 2019"
matchObj=re.search("([a-zA-Z]+)(\s)+(\d+)",s1)

if matchObj !=None:
    print "Entire Match Content = ",matchObj.group() #ormatchObj.group(0)
    print "First group Match Content = ",matchObj.group(1)
    print "Second group Match Content = ",matchObj.group(2)
    print "Third group Match Content = ",matchObj.group(3)
else:
    print "Match NOT Found"



