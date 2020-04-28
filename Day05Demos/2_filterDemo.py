""" filter """

nums = [12,666,20,55,700,9999]
numless100 = [] #get all those elements less than 100

# 1) by list comprehension

numless100 = [i for i in nums if i<100]
print "Original nums = ",nums
print "List with numbers less than 100 = ",numless100   #[12, 20, 55]
print "-------------------------------------------------"

# 2) alternative solution by filter call

def lessnumber(num):
    return num<100 #True or False

numless100 = filter(lessnumber,nums)
print "List with numbers less than 100 = ",numless100   #[12, 20, 55]
print "-------------------------------------------------"

# 3) alternative solution by filter call with lambda

numless100 = filter(lambda x: x<100 ,nums)
print "List with numbers less than 100 = ",numless100   #[12, 20, 55]
print "-------------------------------------------------"
