


from array import array
a = array('H', [4000, 10, 700, 22222])  #from the module "array", array() class is called
print a
print sum(a)        #26932
print "------------------------------------"
print dir(array)
print "------------------------------------"
array.reverse(a)
print a


'''
The array module provides an array() object that is like a list that
stores only homogeneous data and stores it more compactly.
'''





















#print a[1:3]
#array('H', [10, 700])
