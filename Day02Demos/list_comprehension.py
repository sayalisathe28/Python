"""List Comprehension"""

nums=[1,2,3,4,5]
target_list=[]
for i in nums:
    target_list.append(i**2)

print "Original List = ",nums
print "Target Square list = ",target_list
print "======================================"

#2) alternative solution - list comprehension

target_list2=[i**2 for i in nums]               #[1,4,9,16,25]
print "Target square list = ",target_list2
print "======================================"

target_list3=[i**2 for i in nums if i<4]        #[1,4,9]
print "Target square list = ",target_list3      #[1,4,9]
print "======================================="

words=["abc","wyz",123,"lmn",989,"ddfgf67"]
upperwords=[w.upper() for w in words if type(w)==str and w.isalpha()]
print "Original words = ",words
print "Upper words = ",upperwords

print "========================================="
words2=["ABC","xyz","NIL","123","vbfsday123"]
upper_elements=[w for w in words2 if type(w)==str and w.isalpha() and w.isupper()]
print "Original words2 = ",words2
print "Upper words = ",upper_elements
