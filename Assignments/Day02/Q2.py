celsius=[39.2,36.5,37.3,37.8]

def celToFnt(x):
   return (float(9)/5)*x + 32

print "=============================================="
print "Using Map.........."
print "=============================================="

fahrenheit=map(celToFnt,celsius)

print "Temperature in celsius = ",celsius
print "Temperature in Fahrenheit = ",fahrenheit

def fntToCel(x):
    return (float(5)/9)*(x - 32)

celsius=map(fntToCel,fahrenheit)

print "Temperature in celsius = ",celsius

#--------------------------------------------------------------------

print "=============================================="
print "Using Map and lambda.........."
print "=============================================="

celsius=[39.2,36.5,37.3,37.8]
fahrenheit=map(lambda x: (float(9)/5)*x + 32,celsius)

print "Temperature in celsius = ",celsius
print "Temperature in Fahrenheit = ",fahrenheit

celsius=map(lambda x:(float(5)/9)*(x - 32),fahrenheit)
print "Temperature fahrenheit to celsius = ",celsius
