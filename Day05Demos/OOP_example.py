class Circle:

    pi=3.14159
    count=0
    def __init__(self,r):
        self.radius=r
        Circle.count+=1

    def area(self):
        return Circle.pi * (self.radius **2)

if __name__ == "__main__":

    obj1=Circle(2)
    print "Area of Circle 1 = ",obj1.area()

    obj2=Circle(3)
    print "Area of Circle 2 = ",obj2.area()

    obj3=Circle(4)
    print "Area of Circle 3 = ",obj3.area()

    print "Total no of Circle objects = ",Circle.count
