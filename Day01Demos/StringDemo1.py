#!c:\python27

"""
String objects in python
"""

s1='A"BC'
print "S1 = ",s1 #A"BC

s2="x'yz"
print "S2 = ",s2 #x'yz

#s3='A'BC' #SyntaxError
#s33="A"BC" #SyntaxError
s3='A\'BC'
print "S3 = ",s3 #A'BC

#s4="A\"BC"
#print "S4 = ",s4 #A"BC

s4=""" A'B"C """
print "S4 = ",s4 #A'B"C


s5=""" Welcome
        to
            Pune"""
print "S5 = ",s5

path1="c:\new\test.txt"
print "Path1 = ",path1 

path1="c:\\new\\test.txt"
print "Path1 = ",path1 #c:\new\test.txt

#raw string definition in Python
path2 = r"c:\new\test.txt"    #or R'string text'
print "Path2 = ",path2 #c:\new\test.txt

s1="ABC"
print "Type of s1 = ",type(s1) #<type 'str'>
print "------------------------"

num1=100
print "Type of num1 = ",type(num1)  #<type 'int'>

pi=3.14
print "Type of pi = ",type(pi)  #<type 'float'>


