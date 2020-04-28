"""
re.search()
Search at End
using ^ and $
Special Meta characters : ^ $ . | [ ] { } ( ) + * ?

Eg:
"^pattern$"
^hi$ -> true for only hi
"""

import re

s1="99"         #Match Found content =  99
s1="aa99bb"     #Match NOT Found!!!!
s1="99aaa99"    #Match NOT Found!!!!

matchObj = re.search(r"^99$",s1,re.IGNORECASE)

if matchObj != None:
    print "Match Found content = ",matchObj.group()
else:
    print "Match NOT Found!!!!"  


