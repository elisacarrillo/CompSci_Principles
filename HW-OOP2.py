#Define a class named Circle which can be constructed by a radius.
#The Circle class has a method which can compute the area.
import math
class Circle:
    
    
    def __init__(self,r):
        self.r = r

    def area(self):
        
        final = (math.pi)*(self.r**2)
        print("The area for the radius " + str(self.r) + " is " + str(final))

example = Circle(int(input("Put in radius")))
example.area()

        
