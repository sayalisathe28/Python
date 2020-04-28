"""
Sequence Types: mixed object elements collection
Tuple () immutable
List [] mutable
"""

t1=(123,"abc",3.14)
print "tuple 1 = ",t1
print "t1[0] = ",t1[0]
print "type of t1 = ",type(t1)
print "Count of 123 in t1 = ",t1.count(123)
print "Index of abc in t1 = ",t1.index("abc")

#print "Index of bc in t1 = ",t1.index("bc") #ValueError: tuple.index(x): x not in tuple

t2=(123,"abc",3.14,[99,88])
print "Last Element = ",t2[-1]
print "Type of last element = ",type(t2[-1])
print "0th element in iiner list = ",t2[-1][0]
print "Tuple t2 = ",t2
t2[-1][-1]=100
print "Updated list in t2 = ",t2


