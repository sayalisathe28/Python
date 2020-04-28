FH = open(r"target.txt","a")
FH.write("Hello World!!!!\n")
FH.close()
print "---------------------------"

fin=open(r"target.txt","r")
print "While loop....."
print "---------------------------"
while(True):
    line=fin.readline()
    line=line.rstrip()
    if line=="":break
    print line
FH.close()
print "---------------------------"

fin.seek(0)
print "For loop....."
print "---------------------------"
for line in fin:
    line=line.rstrip()
    print line
FH.close()
print "---------------------------"
