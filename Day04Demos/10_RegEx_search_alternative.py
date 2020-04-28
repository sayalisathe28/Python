"""
re.search()
search for alternative options

Eg:
"pattern1|pattern2|pattern3"

"""

import re

s1="\n Welcome to PSL, Wipro, Infosys"  #Match Found content =  PSL

matchObj = re.search(r"Infosys|Wipro|PSL",s1)   #search traverses once so 1st PSL is found
#matchObj = re.search(r"Infosys|Wipro|^PSL",s1)  #Match Found content =  Wipro
if matchObj != None:
    print "Match Found content = ",matchObj.group()
else:
    print "Match NOT Found!!!!"  


