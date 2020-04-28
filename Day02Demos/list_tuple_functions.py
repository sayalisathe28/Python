list1=[1,2,3,4,5]
newtuple=tuple(list1) #list1 is converted to tuple
print "list1 = ",list1 #[1, 2, 3, 4, 5]
print "newTuple = ",newtuple   #(1, 2, 3, 4, 5)

print "ID of list1 = ",id(list1) #48773840
print "ID of New tuple = ",id(newtuple) #41639296

print "================================================"

t1=(10,20,30)
newlist=list(t1) #converts tuple t1 to a new list
print "Tuple = ",t1
print "New list = ",newlist

# tuple inside tuple ==== same memory

print "================================================"

t2=(None,)
t3=(100,)
t4=1,2,34,3 #default to tuplr definition

print "t4 = ",t4
print "Type of t4 = ",type(t4)

print "================================================"
#SWAPPING
a=100
b=200
print "a = %d b = %d "%(a,b)
a,b=b,a
print "a = %d b = %d "%(a,b)
