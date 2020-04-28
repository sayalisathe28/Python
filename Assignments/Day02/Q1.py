list1=[47,11,42,102,13]

def findbig(x,y):
    if x>y: return x
    else : return y

print "Original List = ",list1
print "Largest Number = ",reduce(findbig,list1)
