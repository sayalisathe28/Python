
import re

input1=raw_input("Enter a number")

matchObj = re.search(r"^[0-9]$",input1)

if matchObj != None:
    print "Match Found content = ",matchObj.group()
else:
    print "Match NOT Found!!!!"  


"""
Assignment :
Accept single digit number from keyboard and validate it to be exact 1 digit ^[0-9]$
"""
