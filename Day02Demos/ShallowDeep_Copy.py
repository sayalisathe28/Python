
import copy

"""
Shallow copy, deep copy
"""

list1=[1,2,3,4,5]
print "Original list = ",list1
print "Id of list1 = ",id(list1)    #51264208


newlist1=list1 #shallow copy (same content and id)
print "New list1 = ",newlist1
print "Id of list1 = ",id(newlist1) #51264208
list1.append([99,88])
print "Changed list1 = ",list1
print "New List1 is changed = ",newlist1

print "---------------------------------------------"

#deep copy
list2=[1,2,3,4,5]
newlist2=copy.deepcopy(list2) # two separate memories are maintained
print "list2 = ",list2
print "Id of list2 = ",id(list2)

print "new list2 = ",newlist2
print "Id of newlist2 = ",id(newlist2)

list2.append(1000)
print "Changed list2 = ",list2
print "newlist2 is not changed = ",newlist2
print "---------------------------------------------"

list3=[1,2,3]
newlist3=list3[:]
print "Id of list3 = ",id(list3)
print "Id of newlist3 = ",id(newlist3)
