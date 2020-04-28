"""
re.search()
Search at End
use special meta character $
Special Meta characters : ^ $ . | [ ] { } ( ) + * ?

Eg:
"pattern$"

"""

import re
#s1="Welcome to aaaPSL. 99"         #Match NOT Found!!!!
#s1="Welcome to aaaPSL"             #Match Found content = PSL
s1="psl Welcome to"                 #Match NOT Found!!!!

matchObj = re.search(r"PSL$",s1,re.IGNORECASE)      
if matchObj != None:
    print "Match Found content = ",matchObj.group()
else:
    print "Match NOT Found!!!!"  


