"""
Sequence type data structures :
String, Tuple - immutable
List - mutable

slicing expressions
"""

s1="012345"
print "s1 = ",s1
print "First char = ",s1[0]
print "Last char = ",s1[-1]
size=len(s1)
print "Number if char in s1 = ",size
print "s1[2:5] = ",s1[2:5]
print "s1[2:] = ",s1[2:]
print "s1[4:] = ",s1[4:]
print "s1[::-1] = ",s1[::-1]
print "s1[::2] = ",s1[::2]

print "s1[2:5:-1] = ",s1[2:5:-1] #blank o/p
print "s1[5:2:-1] = ",s1[5:2:-1] #543

s1="Hello"
print "Before concatenation s1 = ",s1 #Hello
print "Id of s1 = ",id(s1)  #48967936

s1=s1+"World"
print "After concatenation s1 = ",s1 #Hello World
print "Id of s1 = ",id(s1)  #47525120

print "-------------------------------------"
num1=100
print "Num1 = ",num1
print "Id od num1 = ",id(num1)

num1=99
print "Num1 = ",num1
print "Id od num1 = ",id(num1)
