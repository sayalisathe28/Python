"""
re.search()
By ignore case
use the flag parameter
re.IGNORECASE or re.I
"""

import re
s1="Welcome to PSL" #"Match Found content = PSL"
s1="PSL Welcome to aaaPSL" #"Match Found content = PSL"
s1="Welcome to psl" #"Match Found content = psl"

matchObj = re.search("PSL",s1,re.IGNORECASE)      #search seraches anywhere
if matchObj != None:
    print "Match Found content = ",matchObj.group()
else:
    print "Match NOT Found!!!!"  


