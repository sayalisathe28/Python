a=[1,4,9,16,25,36,49,64,81,100]

def even(x):
    if x%2 == 0: return x
    
list1=filter(even,a)
print "=========Using filter and function======"
print list1

list1=filter(lambda x: x%2==0 , a )
print "=========Using filter and lambda======"
print list1
