"""
re.search()
Search at Beginning
use special meta characters
Special Meta characters : ^ $ . | [ ] { } ( ) + * ?

Eg:
"^pattern"

"""

import re
s1="Welcome to PSL"         #Match NOT Found!!!!
#s1="PSL Welcome to aaaPSL" #Match Found content = PSL
#s1="Welcome to psl"        #Match NOT Found!!!!

matchObj = re.search(r"^PSL",s1,re.IGNORECASE)      #search seraches anywhere
if matchObj != None:
    print "Match Found content = ",matchObj.group()
else:
    print "Match NOT Found!!!!"  


