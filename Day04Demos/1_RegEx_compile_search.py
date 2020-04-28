"""
re is a predefined module to write Regular Expressions in Python for
Pattern matches

pattern is a sequential set of characters (alphabets, digits, special characters)
white spaces - manual space bar, tab \n \t \r \f
match() method
"""

import re
s1="Welcome to PSL" #"Match Found!!!!"
#s1="Welcome to aaaPSL" #"Match Found!!!!"
s2="Welcome to psl" #"Match NOT Found!!!!"

#match
#s1="Welcome to aaaPSL 99" #Match NOT Found!!!!

patternObj = re.compile("PSL")
#matchObj = patternObj.search(s1)    #search returns a match object on SUCCESS else None
matchObj = patternObj.match(s1)      #match matches at the beginning only

if matchObj != None:
    print "Match Found!!!!"
else:
    print "Match NOT Found!!!!"  

#or (but more logic is needed in case of complex operations)
print "------------------------------------------------------"
s1.index("PSL")     #find()

if "PSL" in s1:
    print "PSL found in s1"
