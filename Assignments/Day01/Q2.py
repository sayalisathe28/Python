import re


list1=[]
FH=open("urls.txt")
while(True):
    line=FH.readline()
    line=line.rstrip()
    list1.append(line)
    if line=="": break
    urls = [w for w in list1 if re.search("^(http://www)\.[a-zA-Z0-9]+(\.com)$",w)!=None]

print "Valid Urls are : "
print urls
