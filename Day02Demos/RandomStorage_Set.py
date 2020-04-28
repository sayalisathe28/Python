"""
Random data storage

1.Sets : Unique elements , stored randomly
s1={int,str}
s2=set()
"""

s1={1,2,3,4,5,5,5}  #5 elememts
print "Set s1 = ",s1 #set([1, 2, 3, 4, 5])
print "Type of s1 = ",type(s1)
#print s1[0] #TypeError: 'set' object does not support indexing

s2=set([3,3,4,5,6])
print "Set s2 = ",s2 #print "Type of s1 = ",type(s1)
print "Type of s2 = ",type(s2)

print "Set Union = ",s1|s2 #Set Union =  set([1, 2, 3, 4, 5, 6])
print "Set Intersection = ",s1&s2 #Set Intersection =  set([3, 4, 5])

s4={1,2,3,4}
print "s1 = ",s1
s4.add(22)
print "s1 = ",s1


s3={}   #DICTIONARY
print "s3 = ",s3 #{}
print "Type of s3 = ",type(s3)
