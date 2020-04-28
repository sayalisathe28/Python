pi=3.141459
def area(r):
    global pi
    return (pi*r*r)

def fib(n):
    a,b=0,1
    while b < n:
        print b
        a,b=b,a+b #tuple
        
print "In mymath, name of the module = ",__name__  #__main__
if __name__ == "__main__":  #
    print "========================================"
    print "In mymath, name of the module = ",__name__
    fib(21)
    print area(5)
    print "========================================"
