""" File Handling """

FH = open("data.txt")   #open function return file handle/object in default read
#IOError: [Errno 2] No such file or directory: 'data.txt'
#print dir(FH)
line1=FH.readline()
line1=line1.rstrip()
print "Line1 = ",line1

str1 = FH.read()
print str1
#OR
"""
line2=FH.readline() #read 2nd line bcz cursor is at end of 1st line
print "Line2 = ",line2

line3=FH.readline()
print "Line3 = ",line3
"""
#OR
print "=================================="
print "Current FH Position = ",FH.tell()    #68
FH.seek(0)
print FH.readlines()
FH.seek(1)
print FH.readlines()

print "==================================="
FH.seek(0)
str1 = FH.read(7)
print str1

FH.close()
