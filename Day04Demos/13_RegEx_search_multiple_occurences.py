"""
re.search()
multiple occurances :
{num}
{min,max}
{min,}
exact4 digit entry from keyboard

"\d{4}"
"^\d{4}$"
"^[0-9]$"

validate the keyboard price field
1. begin with $
2. at least 1 digit after this$
3. . after above digit/s
4. after. , exact 2 number of digits
"$5.66" Valid
".55" Not valid
"$34.33456" not valid

pattern="^\$\d+\.\d{2}$"

\. or for dot =[.]
"""

import re

s1="xyyyyz"  #Match Found content =  xyyyyz
s1="xyz"    #Match NOT Found!!!!
matchObj = re.search(r"xy{4}z",s1)


if matchObj != None:
    print "Match Found content = ",matchObj.group()
else:
    print "Match NOT Found!!!!"  


