"""
Sequence Types: mixed object elements collection
Tuple () immutable
List [] mutable
"""

t1=(123,"abc",3.14)
print "tuple 1 = ",t1
print "t1[0] = ",t1[0]
print "type of t1 = ",type(t1)
#print t1[3] #IndexError: tuple index out of range
#t1[1]=99 #TypeError: 'tuple' object does not support item assignment
print "---------------------"

list1=[123,"abc",3.14]
print "List1 1 = ",list1
print "list1[0] = ",list1[0]
print "type of list1 = ",type(list1)
list1[1]="float replacer"
print "Updated list = ",list1
print "---------------------"

result=list1.append([99,88]) #result is None
print "Updated List = ",list1 #Updated List =  [123, 'float replacer', 3.14, [99, 88]]

result=list1.extend([77,66])
print "Updated List = ",list1#Updated List =  [123, 'float replacer', 3.14, [99, 88], 77, 66]

list1.sort()
print "Sorted List = ",list1

list1.reverse()
print "Reversed List = ",list1

list1.remove(123)
print list1 #element ot present then -ValuError

list2=[10,3,2,134]
list2.sort()
print list2

list2=[10,3,2,134,'z','a']
list2.sort()
print list2

list2=[10,3,2,134,[22,11],'z','a','xyz']
list2.sort()
print list2

list2=[10,3,2,134,[22,11],'z','a','xyz',['s','a','d']]
list2.sort()
print list2

list2=[10,3,2,3.14,134,[22,11],'z','a','xyz']
list2.sort()
print list2

list2=[10,3,2,3.14,134,[22,11],'z','a','xyz']
list2.sort(reverse=True)
print list2

list2=['sayali','xyz','abcd']
print "Before sort ",list2
list2.sort()
print "After sort ",list2

list2=['sayali','xyz','abcd']
print "Before sort ",list2
list2.sort(key=len) #functional programming
print "Sorted words by length = ",list2

#if u dont want to modify original list
nums=[99,55,1,45]
#nums.sort(key=len) #TypeError bcz nums do not have length
sorted_list1=sorted(nums)
print "Original List = ",nums
print "Sorted List = ",sorted_list1

nums=[99,55,1,45]
list_iter=reversed(nums)
#print list_iter

nums=[99,55,1,45]
nums.reverse()
print nums

#In 
print 99 in nums #True
print 199 in nums #False
print 199 not in nums #True

s1="100"
num1=int(s1)

s1="A"
#num1=int(s1)#ValueError: invalid literal for int() with base 10: 'A'
