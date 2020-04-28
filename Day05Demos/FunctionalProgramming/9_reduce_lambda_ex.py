#reduce, lambda
print reduce(lambda x,y: x+y, [47,11,42,13])    #113
print "--------------------------------------------------"

#example:get maximum number from a list  : reduce and lambda
list1 = [47,11,42,102,13]   #greater number =102
f = lambda a,b: a if (a > b) else b
print reduce(f, [47,11,42,102,13])   #102



