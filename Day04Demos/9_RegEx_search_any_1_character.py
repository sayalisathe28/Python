"""
re.search()
using . 

Eg:
"PSL." at the end
"""

import re
#validate s1 if it contains PSL. at the end

s1="\n Welcome to PSL."  #Match Found content = PSL
s1="\n Welcome to PSL*"  #Match Found content =  PSL* for "PSL."
s1="\n Welcome to PSL*"  #Match NOT Found!!!!

matchObj = re.search(r"PSL\.",s1,re.IGNORECASE)

if matchObj != None:
    print "Match Found content = ",matchObj.group()
else:
    print "Match NOT Found!!!!"  


