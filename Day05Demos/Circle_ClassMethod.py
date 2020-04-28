class Circle:

    pi=3.14159
    all_circles=[]  #class variable list

    def __init__(self,r=1):
        self.radius=r
   
    def area(self):
        return Circle.pi * (self.radius **2)

    @classmethod
    def total_area(cls):    #cls is catching argumnet as Classname --> here Circle but useful when there are multiple classes
        total=0
        for c in cls.all_circles:
            total=total+c.area()
        return total
        

obj1=Circle(2)
obj2=Circle(3)
obj3=Circle(4)

Circle.all_circles=[obj1,obj2,obj3]

print "Total no of Circle objects = ",Circle.total_area()   #when class method is called, Classname is passed implicitly to total_area()

