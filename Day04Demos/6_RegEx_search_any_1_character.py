"""
re.search()
Search for any 1 single character except \n
using . 

Eg:
"."
"""

import re

s1="Welcome to PSL"    #Match Found content =  W
s1="* Welcome to PSL"   #Match Found content =  *
s1="\n Welcome to PSL"  #Match Found content =   (space after \n)
matchObj = re.search(r".",s1,re.IGNORECASE)

if matchObj != None:
    print "Match Found content = ",matchObj.group()
else:
    print "Match NOT Found!!!!"  


