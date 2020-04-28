r=[0,1,2,3,4,5,6]

def sum(x,y):
    return x+y

ans=sum(10,20)
print "Addition of 10 and 20 = ",ans    #30
print "-------------------------------------------"

print reduce(sum,r)     #21  sum(0,1)=1  sum(1,2)=3 sum(3,3)
print "-------------------------------------------"
print reduce(lambda x,y: x+y,r)
print "-------------------------------------------"


def plus(x,y):
    return (x+y)


