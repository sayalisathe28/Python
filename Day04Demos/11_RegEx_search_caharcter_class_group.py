"""
re.search()
character class group []
search for any one single charcter out of group pf characters

Eg:
"a|b|c|d" or [abcd] or [a-d]
"0|1|2|3|4|5"
[a-z]
[0-9]
[a-zA-Z]
[]- inside this all special meta character acts like a alphabet
[*+|?] plain text char, exception ^
[^0-9] Negation of digit group
alphanumeric word character [a-zA-Z0-9_]  or  \w
Non alphanumeric word character [^a-zA-Z0-9_]  or  \W
Digit match [0-9] or \d
Non Digit match [^0-9] or \D
white space match [ \n\t\r\f] or \s
Non white space match [^ \n\t\r\f] or \S
"""

import re

s1="Welcome to PSL, Wipro, Infosys 2019"  

matchObj = re.search(r"\d",s1)        #Match Found content =  2
matchObj = re.search(r"\d+",s1)       #Match Found content =  2019
matchObj = re.search(r"[a-zA-Z]+",s1) #Match Found content =  Welcome
if matchObj != None:
    print "Match Found content = ",matchObj.group()
else:
    print "Match NOT Found!!!!"  


"""
Assignment :
Accept single digit number from keyboard and validate it to be exact 1 digit ^[0-9]$
"""
