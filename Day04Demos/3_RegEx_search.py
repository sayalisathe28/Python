"""
re is a predefined module to write Regular Expressions in Python for
Pattern matches

pattern is a sequential set of characters (alphabets, digits, special characters)
white spaces - manual space bar, tab \n \t \r \f
match() method
"""

import re
s1="Welcome to PSL" #"Match Found!!!!"
s1="PSL Welcome"
#matchObj = re.match("PSL",s1)      #match matches at the beginning only

s1="Welcome to PSL"
matchObj = re.search("PSL",s1)      #search seraches anywhere
if matchObj != None:
    print "Match Found content = ",matchObj.group()
else:
    print "Match NOT Found!!!!"  


