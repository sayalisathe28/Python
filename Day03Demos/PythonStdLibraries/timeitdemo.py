

from timeit import Timer   #Timer is  a class
t1 = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit() #timeit() method of class Timer
print "t1 =", t1
#0.57535828626024577
t2 = Timer('a,b = b,a', 'a=1; b=2').timeit()
print "t2 =", t2 
#0.54962537085770791
