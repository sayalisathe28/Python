"""Dictionary Comprehension"""

list1=[1,2,3,4]
new_dict={i:i**2 for i in list1}   #{1:1,2:4,3:9,4:16}
print "Original list = ",list1
print "New Dictionary = ",new_dict
print "========================================="

list1=[1,2,3,4]
new_dict={i:i**2 for i in list1 if i<4}   #{1: 1, 2: 4, 3: 9}
print "Original list = ",list1
print "New Dictionary = ",new_dict
