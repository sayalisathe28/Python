

class Circle:
    pi = 3.14159   #class variable
    all_circles = []  #class variable  list
    def __init__(self, radius):
        self.radius = radius
    def area(self):                                     #instance method
        return self.radius * self.radius * Circle.pi

    @classmethod
    def total_area(cls):    #cls is catching argument as Classname  ---> Circle
        total = 0
        for c in cls.all_circles:
            total = total + c.area()
        return total
    
print "---------------------------------------------------------------------"

c1 = Circle(1)
c2 = Circle(2)
c3 = Circle(3)

Circle.all_circles = [c1,c2,c3]    #list of 2 Circle Objects

#c1.total_area(Circle.all_circles)# c1 is passed as implicit parameter if it is insatnce method
print "Total area = ", Circle.total_area()   #when class method is called, Classname itself is passed as an implicit parameter



#

#print "Area= ", c1.area()
#print "Area= ", c2.area()






























































