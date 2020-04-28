"""
re.search()
wildcard metacharacters :

+ 1 or more
* 0 or more
? 0 or 1 only
"""

import re

s1="xyyz"  #Match Found content =  xyyz
s1="xz"    #Match NOT Found!!!!
matchObj = re.search(r"xy+z",s1)

s1="xyyyz" #Match NOT Found!!!!
s1="xyxyz" #Match Found content =  xyxyz
matchObj = re.search(r"(xy)+z",s1)

if matchObj != None:
    print "Match Found content = ",matchObj.group()
else:
    print "Match NOT Found!!!!"  


