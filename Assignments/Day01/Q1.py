import re

list1=[]
FH=open("emails.txt")
while(True):
    line=FH.readline()
    line=line.rstrip()
    list1.append(line)
    if line=="": break
    alphabetical_words = [w for w in list1 if re.search("^([a-zA-Z0-9_]+)@([a-zA-Z]+)\.([a-z]+)$",w)!=None]

print "Valid Email Addresses are : "
print alphabetical_words
